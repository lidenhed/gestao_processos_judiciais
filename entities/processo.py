class Processo:

    def __init__(self, autor: str, codOAB_advogado_autor: int, data: str, eh_sigiloso: bool, id_processo: int, reu: str, juiz: int):
        self.__autor = autor
        self.__codOAB_advogado_autor = codOAB_advogado_autor
        self.__codOAB_advogado_reu = -1
        self.__data = data
        self.__eh_sigiloso = eh_sigiloso
        self.__eh_urgente = False
        self.__id_processo = id_processo
        self.__reu = reu

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def codOAB_advogado_autor(self):
        return self.__codOAB_advogado_autor

    @codOAB_advogado_autor.setter
    def codOAB_advogado_autor(self, codOAB_advogado_autor):
        self.__codOAB_advogado_autor = codOAB_advogado_autor

    @property
    def codOAB_advogado_reu(self):
        return self.__codOAB_advogado_reu

    @codOAB_advogado_reu.setter
    def codOAB_advogado_reu(self, codOAB_advogado_reu):
        self.__codOAB_advogado_reu = codOAB_advogado_reu
