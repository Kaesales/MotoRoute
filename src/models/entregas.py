


class Entrega():
    def __init__(self, codigo:str, nome_destinatário: str, cpf: str, endereco: str, numero: str, bairro: str, cidade:str):
        self.cod = codigo
        self.nome_destinatario = nome_destinatário
        self.cpf = cpf
        self.endereco = endereco
        self.numero = numero
        self.bairo = bairro
        self.cidade = cidade
        self.entregador = None

