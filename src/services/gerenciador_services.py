from src.dao.gerenciador_dao import GerenciadorDAO
from src.dao.entrega_dao import EntregaDAO
from src.dao.entregador_dao import EntregadorDAO
from src.models.entregador import Entregador
from src.models.entregas import Entrega
from src.models.gerenciador import Gerenciador
from typing import List
from datetime import date

class GerenciadorService():
    
    @classmethod
    def criar_gerenciador(cls, nome:str, data_nascimento: date, cpf: str):

        validacao = GerenciadorDAO.buscar_por_cpf(cpf)
    
        if validacao:
            return("o CPF fornecido já está cadastrado no sistema")
        
        gerenciador = Gerenciador(nome, data_nascimento, cpf)
        GerenciadorDAO.adicionar_gerenciador(gerenciador)
        return gerenciador

    @classmethod
    def listar_gerenciadores() -> List[Gerenciador]:
        return GerenciadorDAO.listar_gerenciadores()
    
    @classmethod
    def create_entregador(cls, nome: str, data_nascimento: date, cpf: str, email:str) -> Entregador:

        validacao = EntregadorDAO.buscar_por_cpf(cpf)
        if validacao:
            raise ValueError("o CPF fornecido já está cadastrado no sistema")
        
        entregador = Entregador(nome, data_nascimento, cpf, email)
        EntregadorDAO.adicionar_entregador(entregador)
        return entregador

    @classmethod
    def update_entregador(cls, cpf:str, nome_atualizado: str, data_nascimento_atualizada: date, cpf_atualizado: str, email_atualizado:str):
        entregador = EntregadorDAO.buscar_por_cpf(cpf)
        
        if not entregador:
            raise ValueError("Nenhum entregador foi encontrado com o cpf fornecido")
        
        entregador.nome = nome_atualizado
        entregador.data_nascimento = data_nascimento_atualizada
        entregador.cpf = cpf_atualizado
        entregador.email = email_atualizado

        EntregadorDAO.atualizar(entregador)
        
        
    @classmethod
    def listar_entregadores() -> List[Entregador]:
        return EntregadorDAO.listar_entregadores()
    
    
    @classmethod
    def atribuir_entrega(cls, entrega_cod: int, entregador_cpf: str):
        """
        Atribui uma entrega a um entregador específico, validando ambos.

        :param entrega_id: ID da entrega a ser atribuída.
        :param entregador_cpf: CPF do entregador que realizará a entrega.
        :raises ValueError: Se a entrega ou o entregador não forem encontrados.
        """
        # Buscar a entrega no DAO
        entrega = EntregaDAO.buscar_por_id(entrega_cod)
        if not entrega:
            raise ValueError("Entrega não encontrada.")

        # Buscar o entregador no DAO
        entregador = EntregadorDAO.buscar_por_cpf(entregador_cpf)
        if not entregador:
            raise ValueError("Entregador não encontrado.")

        # Atribuir entrega ao entregador
        entrega.entregador = entregador
        entregador.entregas.append(entrega)


        