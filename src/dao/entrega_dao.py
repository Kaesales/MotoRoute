from src.models.entregas import Entrega
from typing import List

class EntregaDAO:
    __data: List[Entrega] = []
    
    @classmethod
    def adicionar_entrega(cls, entrega: Entrega):
        cls.__data.append(entrega)

    @classmethod
    def listar_entregas(cls) -> List[Entrega]:
        return cls.__data

    @classmethod
    def buscar_por_codigo(cls, codigo: str):
        return next((item for item in cls.__data if item.codigo == codigo), None)
    
    @classmethod
    def atualizar(cls, entrega:Entrega):
        # Aqui, como o objeto já está em `_data`, não precisa fazer nada.
        # Este método pode ser útil para explicitamente salvar em um banco de dados.
        pass

    @classmethod
    def pegar_entregas_entregador(cls, cpf: str):
        return next((item for item in cls.__data if item.entregador == cpf), None)

    
    @classmethod
    def deletar(cls, entrega):
        cls.__data.remove(entrega)