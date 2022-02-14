from interface.processo import InterfaceProcesso
from arquivos.processoDAO import ProcessoDAO
from controllers.validadorCPF import ValidadorCPF

class ProcessoController:

    def __init__(self, controlador_execucao):
        self.__interface_processo = InterfaceProcesso(self)
        self.__processo_dao = ProcessoDAO()
        self.__controlador_execucao = controlador_execucao

    def cadastrar_processo(self):
        return False

    def verifica_cadastro_completo(self, values):
        if values['anexos'] == '' or values['autor'] == '' or values['codOAB_advogado_autor'] == '' or values['eh_sigiloso'] == '' or values['reu'] == '' or:
            self.__interface_processo.close_tela_principal()
            return False
        return True
