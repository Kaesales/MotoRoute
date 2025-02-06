
from pydantic import BaseModel
from typing import List
from src.models.entregas import Entrega
class Entregador(BaseModel):
    nome:str
    data_nascimento: str
    cpf:str
    email: str
    
     
    