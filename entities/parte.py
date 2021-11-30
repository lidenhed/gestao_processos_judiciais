from entities.usuario import Usuario


class Parte(Usuario):

    def __init__(self, nome: str, cpf: str, senha: str, advogado: str, logado: bool = False):
        super().__init__(nome, cpf, senha, logado)
        self.__advogado = advogado

    @property
    def advogado(self):
        return self.__advogado

    @advogado.setter
    def advogado(self, advogado: str):
        self.__advogado = advogado
