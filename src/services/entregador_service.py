from src.dao.entregador_dao import EntregadorDAO
from src.models.entregador import Entregador

from datetime import date

class EntregadorService:
    @staticmethod
    def listar_entregas(entregador):
        """
        Lista as entregas do entregador com validação adicional.
        """
        if not isinstance(entregador, Entregador):
            raise ValueError("O objeto fornecido não é um entregador válido.")
        
        # Aqui você poderia adicionar lógica extra, como:
        # - Filtrar entregas por status (pendente, concluída)
        # - Ordenar entregas por data
        return entregador.entregas
   