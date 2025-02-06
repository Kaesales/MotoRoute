from fastapi import APIRouter, HTTPException, Form
from src.services.gerenciador_services import GerenciadorService


router = APIRouter()

# Criar um gerenciador
@router.post('/gerenciador', status_code=201)
async def criar_gerenciador(
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...)
):
    try:
        GerenciadorService.criar_gerenciador(nome, data_nascimento, cpf, email)
        return {"message": "Gerenciador criado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Listar todos os gerenciadores
@router.get('/gerenciadores', status_code=200)
async def listar_gerenciadores():
    return GerenciadorService.listar_gerenciadores()





