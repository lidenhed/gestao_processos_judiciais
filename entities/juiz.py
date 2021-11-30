from entities.usuario import Usuario


class Juiz(Usuario):

    def __init__(self, nome: str, cpf: str, matricula: int, senha: str, logado: bool = False):
        super().__init__(nome, cpf, senha)
        self.__senha = senha
        self.__logado = logado
        self.__matricula = matricula

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
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula
