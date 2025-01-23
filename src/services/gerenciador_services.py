from src.dao.gerenciador_dao import GerenciadorDAO
from src.models.gerenciador import Gerenciador
from src.services.entregador_services import EntregadorService
from typing import List
from datetime import date

class GerenciadorService:
    
    @classmethod
    def criar_gerenciador(cls, nome:str, data_nascimento: str, cpf: str, email: str):

        validacao = GerenciadorDAO.buscar_por_cpf(cpf)
    
        if validacao:
            return("o CPF fornecido já está cadastrado no sistema")
        
        gerenciador = Gerenciador(nome = nome, data_nascimento = data_nascimento, cpf = cpf, email = email)
        GerenciadorDAO.adicionar_gerenciador(gerenciador)
        return gerenciador

    @classmethod
    def listar_gerenciadores(cls) -> List[Gerenciador]:
        return GerenciadorDAO.listar_gerenciadores()
    
   
    
    @classmethod
    def deletar_gerenciador(cls, id_gerenciador: int) -> str:
        gerenciador = GerenciadorDAO.buscar_por_id(id_gerenciador)
        if not gerenciador:
            raise ValueError("Gerenciador não encontrado com o ID fornecido.")
        
        GerenciadorDAO.deletar(gerenciador)
        return f"Gerenciador com ID {id_gerenciador} foi deletado com sucesso."