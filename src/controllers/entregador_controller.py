from fastapi import APIRouter, HTTPException
from src.services.entregador_service import EntregadorService
from datetime import date

router = APIRouter()

@router.post('/entregador')
def create_entity(nome:str, data_nascimento: date, cpf: str):
    try:
        EntregadorService.criar_entregador(nome, data_nascimento, cpf)
        return{"message": "Entity created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/entity1/")
def list_entity1():
    return EntregadorService.listar_entregadores()
