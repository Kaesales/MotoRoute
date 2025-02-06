from pydantic import BaseModel
from typing import List

class Gerenciador(BaseModel):
    nome:str
    data_nascimento: str
    cpf:str
    email: str
     