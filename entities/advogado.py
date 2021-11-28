from entities.usuario import Usuario


class Advogado(Usuario):

    def __init__(self, nome: str, cpf: str, login: str , senha: str, logado: bool):
        
        super().__init__(nome, cpf, login, senha, logado)

