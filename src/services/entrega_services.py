from src.dao.entrega_dao import EntregaDAO
from src.models.entregas import Entrega

class EntregaService():
    @classmethod
    def criar_entrega(codigo:str, nome_destinatário:str, cpf:str, enderec:str, numero:str, bairro:str, cidade:str)
        entrega = Entrega(codigo nome_destinatário, cpf, endereco, numero, bairro, cidade)    
        EntregaDAO.create_entrega(entrega)

    @classmethod
    def listar_entregas():
        return EntregaDAO.listar_entregas()   