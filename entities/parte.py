from entities.usuario import Usuario


class Parte(Usuario):

    def __init__(self, nome: str, cpf: str, senha: str, advogado: str, logado: bool = False):
        super().__init__(nome, cpf, senha)
        self.__senha = senha
        self.__advogado = advogado
        self.__logado = logado

    @property
    def senha(self):
        return self.__senha

    @property
    def logado(self):
        return self.__logado

    @logado.setter
    def logado(self, logado: bool):
        self.__logado = logado

    @property
    def advogado(self):
        return self.__advogado

    @advogado.setter
    def advogado(self, advogado: str):
        self.__advogado = advogado
