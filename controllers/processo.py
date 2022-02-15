from interface.processo import InterfaceProcesso
from arquivos.processoDAO import ProcessoDAO
from controllers.validadorCPF import ValidadorCPF
from controllers.execucao import ControladorSistema

class ProcessoController:

    def __init__(self, controlador_execucao):
        self.__interface_processo = InterfaceProcesso(self)
        self.__processo_dao = ProcessoDAO()
        self.__controlador_execucao = controlador_execucao
        self.__controlador_sistema = ControladorSistema()

    def cadastrar_processo(self):
        tela_cadastro = self.__interface_processo.tela_cadastrar_processo()
        cadastro_ok = self.verifica_cadastro_completo(valores)
        return False

    def verifica_cadastro_completo(self, values):
        if values['anexos'] == '' or values['autor'] == '' or values['codOAB_advogado_autor'] == '' or values['eh_sigiloso'] == '' or values['reu'] == '':
            self.__interface_processo.close_tela_principal()
            return False
        return True
