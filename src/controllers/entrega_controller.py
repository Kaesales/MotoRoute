from fastapi import APIRouter, HTTPException, Form
from src.services.entrega_services import EntregaService

router = APIRouter()


   
@router.get('/entregas')
def listar_entregas():
    try:
        entregas = EntregaService.listar_entregas()
        return entregas
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post('/entrega/{cod_entrega}/{cpf_entregador}')
async def atribuir_entrega(cod_entrega: str, cpf_entregador: str):
    try:
        EntregaService.atribuir_entrega(cod_entrega, cpf_entregador)
        return{"message": "Atribuição realizada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Criar uma entrega
@router.post('/entrega', status_code=201)
async def criar_entrega(
    codigo: str = Form(...),
    nome_destinatario: str = Form(...),
    cpf: str = Form(...),
    endereco: str = Form(...),
    numero: str = Form(...),
    bairro: str = Form(...),
    cidade: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...)
):
    try:
        EntregaService.criar_entrega(codigo, nome_destinatario, cpf, endereco, numero, bairro, cidade, latitude, longitude)
        return {"message": "Entrega criada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Deletar entrega
@router.delete("/entrega/{cod_entrega}", status_code=200)
async def deletar_entrega(cod_entrega: str):
    try:
        mensagem = EntregaService.deletar_entrega(cod_entrega)
        return {"message": mensagem}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
