from src.models.gerenciador import Gerenciador
from typing import List
from datetime import date

class GerenciadorDAO:
    __data = List[Gerenciador] = [] 
    
    @classmethod
    def adicionar_gerenciador(cls, gerenciador: Gerenciador):
        cls.__data.append(gerenciador)

    @classmethod
    def listar_gerenciadores(cls):
        return cls.__data
    

    @classmethod
    def buscar_por_cpf(cls, cpf: str):
        return next((item for item in cls._data if item.cpf == cpf), None)
    
    @classmethod
    def atualizar(cls, gerenciador:Gerenciador):
        # Aqui, como o objeto já está em `_data`, não precisa fazer nada.
        # Este método pode ser útil para explicitamente salvar em um banco de dados.
        pass
