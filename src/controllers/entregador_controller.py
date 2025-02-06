from fastapi import APIRouter, HTTPException, Form, Query
from src.services.entregador_services import EntregadorService
from src.services.entrega_services import EntregaService

router = APIRouter()

# Criar um entregador
@router.post('/entregador', status_code=201)
async def criar_entregador(
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...)
):
    try:
        EntregadorService.criar_entregador(nome, data_nascimento, cpf, email)
        return {"message": "Entregador criado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get('/entregas/{cpf}', status_code=200)
async def listar_entregas(cpf: str):
    """
    Lista as entregas atribuídas a um entregador específico.
    """
    entregas = EntregaService.listar_entregas_por_entregador(cpf)
    
    if not entregas:
        return {"message": "Nenhuma entrega encontrada para este entregador", "entregas": []}
    
    return {"entregas": entregas}

# Buscar um entregador pelo CPF
@router.get('/entregador/{cpf}', status_code=200)
async def buscar_entregador(cpf: str):
    entregador = EntregadorService.buscar_entregador(cpf)
    if not entregador:
        raise HTTPException(status_code=404, detail="Entregador não encontrado")
    return entregador

# Deletar entregador
@router.delete("/entregador/{cpf}", status_code=200)
async def deletar_entregador(cpf: str):
    try:
        mensagem = EntregadorService.deletar_entregador(cpf)
        return {"message": mensagem}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
# Listar todos os entregadores
@router.get('/entregadores', status_code=200)
async def listar_entregadores():
    return EntregadorService.listar_entregadores()

# Atualizar entregador
@router.put('/entregador/{cpf}', status_code=200)
async def atualizar_entregador(
    cpf: str,
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf_atualizado: str = Form(...),
    email: str = Form(...)
):
    try:
        entregador = EntregadorService.buscar_entregador(cpf)
        if not entregador:
            raise HTTPException(status_code=404, detail="Entregador não encontrado")
        
        EntregadorService.atualizar_entregador(cpf, nome, data_nascimento, cpf_atualizado, email)
        return {"message": "Entregador atualizado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/entregador/{cod_entrega}/distancia")
async def calcular_distancia(
    cod_entrega: str, 
    latitude: float = Query(..., description="Latitude do entregador"), 
    longitude: float = Query(..., description="Longitude do entregador")
):
    """
    Calcula a distância entre o entregador e a entrega.
    """
    try:
        resultado = EntregadorService.calcular_distancia(cod_entrega, latitude, longitude)
        
        if "error" in resultado:
            raise HTTPException(status_code=400, detail=resultado["error"])
        
        return resultado
    
    except HTTPException:
        raise  # Mantém HTTPExceptions personalizadas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no cálculo de distância: {str(e)}")
