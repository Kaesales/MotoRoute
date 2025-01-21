from src.models.entregas import Entrega
from typing import List

class EntregaDAO:
    __data = List[Entrega] = []

    @classmethod
    def create_entrega(cls, entrega: Entrega):
        cls.__data.append(entrega)

    @classmethod
    def listar_entregas(cls) -> List[Entrega]:
        return cls.__data

   