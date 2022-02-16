from entities.usuario import Usuario


class Advogado(Usuario):

    def __init__(self, nome: str, login: str, senha: str, logado: bool, cod_OAB):
        super().__init__(nome, login, senha, logado)
        self.__cod_OAB = cod_OAB


