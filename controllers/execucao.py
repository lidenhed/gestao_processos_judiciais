from controllers.juiz import JuizController
from controllers.parte import ParteController
from controllers.Advogado import AdvogadoController
from controllers.processo import ProcessoController
from interface.execucao import InterfaceSistema

class ControladorSistema:
    def __init__(self):
        self.__juiz_controller = JuizController(self)
        self.__parte_controller = ParteController(self)
        self.__advogado_controller = AdvogadoController(self)
        self.__interface_sistema = InterfaceSistema(self)
        self.__processo_controller = ProcessoController(self)

    def juiz_controller(self):
        return self.__controlador_juiz

    def parte_controller(self):
        return self.__parte_controller

    def advogado_controller(self):
        return self.__advogado_controller
    
    def processo_controller(self):
        return self.__processo_controller
    
    def init_module_juiz(self):
        self.__controlador_juiz.cadastrar_juiz()

    def init_module_parte(self):
        self.__parte_controller.cadastrar_parte()

    def init_module_advogado(self):
        self.__advogado_controller.cadastrar_Advogado()
        
    def init_module_cadastrar_processo(self):
        self.__processo_controller.cadastrar_processo()
        
    def init_module_efetuar_ato_processual(self):
        self.__processo_controller.realizar_ato_processual()
        
    def init_module_despachar(self):
        self.__processo_controller.despachar()

    def login(self):
        while True:
            try:
                botao, valores = self.__interface_sistema.tela_login()
                if botao == 'Confirmar':
                    opcao = valores[0]
                    usuario = valores[1]
                    senha = valores[2]
                    if opcao == 'Parte':
                        cadastro = self.parteController.parte_dao.get(usuario)
                    # elif opcao == 'Advogado':
                    #     cadastro = self.advogadoController.advogado_dao.get(usuario)
                    elif opcao == 'Juiz':
                        cadastro = self.controlador_juiz.juiz_dao.get(usuario)
                    if cadastro:
                        if senha == cadastro.senha:
                            return self.__interface_sistema.aviso('Deu certo')
                        else:
                            raise Exception
                    else:
                        raise TypeError
                else:
                    break
            except TypeError:
                self.__interface_sistema.aviso('Escolha um tipo de cadastro e informe seu número de usuário e senha corretamente.')
            except Exception:
                self.__interface_sistema.aviso('Senha incorreta.')

        
