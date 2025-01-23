from src.dao.entrega_dao import EntregaDAO
from src.dao.entregador_dao import EntregadorDAO
from src.models.entregas import Entrega


class EntregaService:
    @classmethod
    def criar_entrega(cls, codigo: str, nome_destinatario: str, cpf: str, endereco: str, numero:str, bairro: str, cidade:str, latitude: float, longitude: float):
        validacao = EntregaDAO.buscar_por_codigo(codigo)
        
        if validacao is not None:
            raise ValueError("Código da entrega inválido. Verifique o código novamente")
        
        entrega = Entrega(
                    codigo=codigo,
                    nome_destinatario=nome_destinatario,
                    cpf=cpf,
                    endereco=endereco,
                    numero=numero,
                    bairro=bairro,
                    cidade= cidade,
                    latitude = latitude,
                    longitude = longitude
        )

        EntregaDAO.adicionar_entrega(entrega)
        return entrega
        
    @classmethod
    def atribuir_entrega(cls, entrega_cod: str, entregador_cpf: str):
        """
        Atribui uma entrega a um entregador específico, validando ambos.

        :param entrega_cod: Código da entrega a ser atribuída.
        :param entregador_cpf: CPF do entregador que realizará a entrega.
        :raises ValueError: Se a entrega ou o entregador não forem encontrados.
        """
        # Buscar a entrega no DAO
        entrega = EntregaDAO.buscar_por_codigo(entrega_cod)
        if not entrega:
            raise ValueError("Entrega não encontrada.")

        # Buscar o entregador no DAO
        entregador = EntregadorDAO.buscar_por_cpf(entregador_cpf)
        if not entregador:
            raise ValueError("Entregador não encontrado.")

        # Atribuir entrega ao entregador
        entrega.entregador = entregador_cpf
        EntregadorDAO.adicionar_entrega(entrega)
        
        # Atualizar as entidades no banco
        EntregaDAO.atualizar(entrega)
        

    @classmethod
    def listar_entregas_por_entregador(cls, cpf: str):
        entregador = EntregadorDAO.buscar_por_cpf(cpf)
        if entregador:
            entregas = EntregaDAO.pegar_entregas_entregador(cpf)
            if not entregas:
                raise ValueError("Não há entregas atribuídas ao entregador")
            return entregas
        
    @classmethod
    def listar_entregas(cls):
            entregas = EntregaDAO.listar_entregas()
            if entregas is not None:
                return entregas
            else:
                raise ValueError("Não há entregas cadastradas")
        
    @classmethod
    def deletar_entrega(cls, cod_entrega: str) -> str:
        entrega = EntregaDAO.buscar_por_codigo(cod_entrega)
        if not entrega:
            raise ValueError("Entrega não encontrada com o código fornecido.")
        
        EntregaDAO.deletar(entrega)
        return f"Entrega com código {cod_entrega} foi deletada com sucesso."