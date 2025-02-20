from interface.juiz import InterfaceJuiz
from arquivos.juizDAO import JuizDAO
from controllers.validadorCPF import ValidadorCPF
import hashlib


class JuizController:
    
    def __init__(self, controlador_execucao):
        self.__interface_juiz = InterfaceJuiz(self)
        self.__juiz_dao = JuizDAO()
        self.__controlador_execucao = controlador_execucao

    def cadastrar_juiz(self):
        while True:
            cpf = ValidadorCPF().solicita_cpf_cadastro()
            if cpf is None:
                break
            existe_cpf = self.verifica_cpf_jah_existente(cpf)
            if existe_cpf:
                self.__interface_juiz.aviso('\nCPF já foi cadastrado!')
                continue
            while True:
                try:
                    valores = self.__interface_juiz.tela_cadastrar_juiz(cpf)
                    cadastro_ok = self.verifica_cadastro_completo(valores)
                except TypeError:
                    break
                if not cadastro_ok:
                    self.__interface_juiz.aviso('\nCampo(s) obrigatórios não preenchidos')
                    continue
                senha = valores['password']
                try:
                    senha_utf = senha.encode('utf-8')
                    sha1hash = hashlib.sha1()
                    sha1hash.update(senha_utf)
                    senha_hash = sha1hash.hexdigest()
                except Exception:
                    self.__tela_login.aviso('Erro ao gerar senha')
                    break
                sucesso_add = self.__juiz_dao.add(valores['nome'],
                                                           cpf,
                                                           senha_hash,
                                                           False)
                if not sucesso_add:
                    self.__interface_juiz.aviso('Erro no cadastro')
                break
            break

    def verifica_cadastro_completo(self, values):
        if values['nome'] == '' or values['password'] == '':
            self.__interface_juiz.close_tela_principal()
            return False
        return True


    def listar_juiz(self):
        dic_nome_num_juizes = {}
        lista_juizes = self.__juiz_dao.get_all()
        for juiz in lista_juizes:
            dic_nome_num_juizes[juiz.nome] = juiz.cpf
        self.__interface_juiz.mostrar_lista(dic_nome_num_juizes)

    def verifica_cpf_jah_existente(self, cpf):
        verificacao = self.__juiz_dao.get(cpf)
        if verificacao is None:
            return False
        return True

    def get_nome_juiz_by_cpf(self, cpf: str):
        juiz = self.__juiz_dao.get(cpf)
        return juiz.nome
