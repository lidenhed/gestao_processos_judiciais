from interface.Advogado import InterfaceAdvogado
from arquivos.advogadoDAO import AdvogadoDAO
from controllers.validadorCPF import ValidadorCPF
import hashlib


class AdvogadoController:
    
    def __init__(self, controlador_execucao):
        self.__interface_Advogado = InterfaceAdvogado(self)
        self.__Advogado_dao = AdvogadoDAO()
        self.__controlador_execucao = controlador_execucao

    def cadastrar_Advogado(self):
        while True:
            cpf = ValidadorCPF().solicita_cpf_cadastro()
            if cpf is None:
                break
            existe_cpf = self.verifica_cpf_jah_existente(cpf)
            if existe_cpf:
                self.__interface_Advogado.aviso('\nCPF já foi cadastrado!')
                continue
            while True:
                try:
                    valores = self.__interface_Advogado.tela_cadastrar_Advogado(cpf)
                    cadastro_ok = self.verifica_cadastro_completo(valores)
                except TypeError:
                    break
                if not cadastro_ok:
                    self.__interface_Advogado.aviso('\nCampo(s) obrigatórios não preenchidos')
                    continue
                cod_OAB = valores['cod_OAB']
                existe_cod_OAB = self.verifica_cod_OAB(cod_OAB)            
                if existe_cod_OAB:
                    self.__interface_Advogado.aviso('\nAdvogado já foi cadastrado!')
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
                sucesso_add = self.__Advogado_dao.add(valores['nome'],
                                                           cpf,
                                                           senha_hash,
                                                           False, cod_OAB)
                if not sucesso_add:
                    self.__interface_Advogado.aviso('Erro no cadastro')
                break
            break

    def verifica_cadastro_completo(self, values):
        if values['nome'] == '' or values['password'] == '':
            self.__interface_Advogado.close_tela_principal()
            return False
        return True


    def listar_Advogado(self):
        dic_nome_num_Advogados = {}
        lista_Advogados = self.__Advogado_dao.get_all()
        for Advogado in lista_Advogados:
            dic_nome_num_Advogados[Advogado.nome] = Advogado.cpf
        self.__interface_Advogado.mostrar_lista(dic_nome_num_Advogados)

    def verifica_cpf_jah_existente(self, cpf):
        verificacao = self.__Advogado_dao.get(cpf)
        if verificacao is None:
            return False
        return True

    def get_nome_Advogado_by_cpf(self, cpf: str):
        advogado = self.__Advogado_dao.get(cpf)
        return advogado.nome
    
    def verifica_cod_OAB(self, cod_OAB):
        verificacao = self.__Advogado_dao.get(cod_OAB)
        if verificacao is None:
            return False
        return True