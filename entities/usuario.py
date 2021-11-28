from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, nome: str, cpf: str, login: str, senha: str, logado: bool = False):
        
        self.__nome = nome
        self.__cpf = cpf
        self.__login = login
        self.__senha = senha
        self.__logado = logado

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
        
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: int):
        self.__senha = senha
        
    @property
    def logado(self):
        return self.__logado

    @logado.setter
    def logado(self, logado: bool):
        self.__logado = logado
