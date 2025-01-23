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
