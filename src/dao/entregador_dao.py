from src.models.entregador import Entregador
from typing import List

class EntregadorDAO:
    __data = List[Entregador] = []


    @classmethod
    def adicionar_entregador(cls, entregador:Entregador):
        cls.__data.append(entregador)

    @classmethod
    def listar_entregadores(cls):
        return cls.__data
    
    @classmethod
    def buscar_por_cpf(cls, cpf: str):
        return next((item for item in cls.__data if item.cpf == cpf), None)
    
    @classmethod
    def atualizar(cls, entregador:Entregador):
        # Aqui, como o objeto já está em `_data`, não precisa fazer nada.
        # Este método pode ser útil para explicitamente salvar em um banco de dados.
        pass
