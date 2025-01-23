from src.dao.entregador_dao import EntregadorDAO
from src.models.entregador import Entregador
from src.dao.entrega_dao import EntregaDAO
from typing import List
from datetime import date
import math


class EntregadorService:
   @classmethod
   def criar_entregador(cls, nome: str, data_nascimento: str, cpf: str, email:str) -> Entregador:

        validacao = EntregadorDAO.buscar_por_cpf(cpf)
        if validacao:
            raise ValueError("o CPF fornecido já está cadastrado no sistema")
        
        entregador = Entregador(nome = nome, data_nascimento = data_nascimento, cpf = cpf, email = email)
        EntregadorDAO.adicionar_entregador(entregador)
        return entregador

   @classmethod 
   def atualizar_entregador(cls, cpf:str, nome_atualizado: str, data_nascimento_atualizada: str, cpf_atualizado: str, email_atualizado:str):
        entregador = EntregadorDAO.buscar_por_cpf(cpf)
        
        if not entregador:
          raise ValueError("Nenhum entregador foi encontrado com o cpf fornecido")
        
        entregador.nome = nome_atualizado
        entregador.data_nascimento = data_nascimento_atualizada
        entregador.cpf = cpf_atualizado
        entregador.email = email_atualizado

        EntregadorDAO.atualizar(entregador)
        
        
   @classmethod
   def listar_entregadores(cls) -> List[Entregador]:
        return EntregadorDAO.listar_entregadores()
    

   @classmethod
   def buscar_entregador(cls, cpf:str) -> Entregador:
        return EntregadorDAO.buscar_por_cpf(cpf)

   @classmethod
   def deletar_entregador(cls, cpf: str) -> str:
        entregador = EntregadorDAO.buscar_por_cpf(cpf)
        if not entregador:
            raise ValueError("Entregador não encontrado com o CPF fornecido.")
        
        EntregadorDAO.deletar(entregador)
        return f"Entregador com CPF {cpf} foi deletado com sucesso."

   @staticmethod
   def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calcula a distância entre dois pontos geográficos (em quilômetros).
        """
        R = 6371  # Raio da Terra em km
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c  # Distância em quilômetros

   @classmethod
   def calcular_distancia(cls, cod_entrega: str, latitude: float, longitude: float) -> dict:
        """
        Calcula a distância entre o endereço atual do entregador e o endereço da entrega.
        """
        entrega = EntregaDAO.buscar_por_codigo(cod_entrega)
        if not entrega:
            return {"error": "Entrega não encontrada."}

        lat1, lon1 = entrega.latitude, entrega.longitude
        lat2, lon2 = latitude, longitude

        # Calcular a distância
        distancia = cls.haversine(lat1, lon1, lat2, lon2)

        return {
            "distancia_km": distancia,
            "entregador_coordenadas": {"latitude": lat2, "longitude": lon2},
            "entrega_coordenadas": {"latitude": lat1, "longitude": lon1},
        }
   