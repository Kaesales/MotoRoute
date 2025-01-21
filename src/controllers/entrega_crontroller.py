from fastapi import APIRouter
from src.services.entrega_services import EntregaService

router = APIRouter()

@router.post('/entrega')
def criar_entrega(nome_destinatário, cpf, endereco, numero, bairro, cidade):
    EntregaService.criar_entrega(nome_destinatário, cpf, endereco, numero, bairro, cidade)
    
@router.get('/entregas')
def listar_entregadores():
    EntregaService.listar_entregas()