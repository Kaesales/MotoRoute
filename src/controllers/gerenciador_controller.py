from fastapi import APIRouter, HTTPException
from src.services.gerenciador_services import GerenciadorService
from datetime import date


router = APIRouter(
)

@router.post('/gerenciador')
def criar_gerenciador(nome: str, data_nascimento: date, cpf:str):
    GerenciadorService.criar_gerenciador(nome, data_nascimento, cpf)

@router.get('/gerenciador')
def pegar_gerenciadores():
    return GerenciadorService.listar_gerenciadores()