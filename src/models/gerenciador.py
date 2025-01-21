from datetime import date


class Gerenciador():
    def __init__(self, nome:str, data_nascimento: date, cpf: str, email:str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.email = email
        