from fastapi import APIRouter, HTTPException, Form
from src.services.gerenciador_services import GerenciadorService
from src.services.entregador_services import EntregadorService
from src.services.entrega_services import EntregaService
from src.models.entregador import Entregador
from datetime import date


router = APIRouter()

@router.post('/gerenciador')
async def criar_gerenciador(
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...)):
    try:
        GerenciadorService.criar_gerenciador(nome, data_nascimento, cpf, email)
        return{"message": "Entity created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/gerenciadores')
async def listar_gerenciadores():
    return GerenciadorService.listar_gerenciadores()


@router.post('/gerenciador/entregador', status_code=201)
async def criar_entregador(
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...)
):
    try:
        EntregadorService.criar_entregador(nome, data_nascimento, cpf, email)
        return{"message": "Entregador criado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/gerenciador/entregadores', status_code=201)
async def listar_entregadores():
    return EntregadorService.listar_entregadores()


@router.put('/gerenciador/{cpf}/atualizar')
async def atualizar_entregador( 
    cpf: str,
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf_atualizado: str = Form(...),
    email: str = Form(...),
    ):
    try: 
        entregador = EntregadorService.buscar_entregador(cpf)
        if entregador:
            EntregadorService.atualizar_entregador(cpf, nome, data_nascimento, cpf_atualizado, email)
            return{"message": "Entity update successfully"}
        else:
            raise ValueError("CPF não encontrado na base de dados")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/gerenciador/{cpf}')
async def buscar_entregador(cpf: str):
    try: 
        entregador = EntregadorService.buscar_entregador(cpf)
        if entregador:
            return entregador
        else:
            raise ValueError("CPF não encontrado na base de dados")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/gerenciador/{cpf}/entregas', status_code=200)
async def listar_entregas_entregador(cpf: str):
    """
    Lista as entregas atribuídas a um entregador específico.
    """
    try:
        entregas = EntregaService.listar_entregas_por_entregador(cpf)
        return {"entregas": entregas}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post('/gerenciador/entrega')
async def criar_entrega(codigo: str = Form(...), nome_destinatario: str=Form(...), cpf: str=Form(...), endereco: str=Form(...), numero:str=Form(...), bairro: str=Form(...), cidade:str=Form(...), latitude: float = Form(...), longitude: float = Form(...)):
    try:
        EntregaService.criar_entrega(codigo, nome_destinatario, cpf, endereco, numero, bairro, cidade, latitude, longitude)
        return{"message": "Entrega criada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.delete("gerenciador/entregador/{cpf}")
async def deletar_entregador(cpf: str):
    try:
        mensagem = EntregadorService.deletar_entregador(cpf)
        return {"message": mensagem}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("gerenciador/entrega/{cod_entrega}")
async def deletar_entrega(cod_entrega: str):
    try:
        mensagem = EntregaService.deletar_entrega(cod_entrega)
        return {"message": mensagem}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))