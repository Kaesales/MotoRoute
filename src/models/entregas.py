from datetime import date
from pydantic import BaseModel
from typing import List, Optional



class Entrega(BaseModel):
    codigo: str           
    nome_destinatario:str
    cpf: str 
    endereco: str              
    numero:str           
    bairro: str            
    cidade: str     
    latitude: float
    longitude: float       
    entregador:str = None

