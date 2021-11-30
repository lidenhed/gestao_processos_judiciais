from entities.usuario import Usuario


class Juiz(Usuario):

    def __init__(self, nome: str, cpf: str, matricula: int, senha: str, logado: bool = False):
        super().__init__(nome, cpf, senha, logado)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula

