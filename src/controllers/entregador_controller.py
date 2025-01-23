from fastapi import APIRouter, HTTPException, Form
from src.services.entregador_services import EntregadorService
from src.services.entrega_services import EntregaService
from datetime import date
from src.models.entregador import Entregador
router = APIRouter()


    

@router.get('/entregas/{cpf}', status_code=200)
async def listar_entregas(cpf: str):
    """
    Lista as entregas atribuídas a um entregador específico.
    """
    try:
        entregas = EntregaService.listar_entregas_por_entregador(cpf)
        return {"entregas": entregas}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    



@router.post("/entregador/{cod_entrega}/distancia")
async def calcular_distancia(cod_entrega: str, latitude: float = Form(...), longitude: float = Form(...)):
    """
    Calcula a distância entre o entregador e a entrega.
    """
    try:
        resultado = EntregadorService.calcular_distancia(cod_entrega = cod_entrega, latitude = latitude, longitude = longitude)
        if "error" in resultado:
            raise HTTPException(status_code=400, detail=resultado["error"])
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
