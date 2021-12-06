from controllers.juiz import JuizController
from controllers.parte import ParteController
from controllers.Advogado import AdvogadoController
from interface.execucao import InterfaceSistema

class ControladorSistema:
    def __init__(self):
        self.__juiz_controler = JuizController(self)
        self.__parte_controller = ParteController(self)
        self.__advogado_controller = AdvogadoController(self)
        self.__interface_sistema = InterfaceSistema(self)

    @property
    def juiz_controler(self):
        return self.__juiz_controler

    @property
    def parte_controller(self):
        return self.__parte_controller

    @property
    def advogado_controller(self):
        return self.__advogado_controller
    
    def init_module_juiz(self):
        self.__juiz_controler.cadastrar_juiz()

    def init_module_parte(self):
        self.__parte_controller.cadastrar_parte()

    def init_module_advogado(self):
        self.__advogado_controller.cadastrar_Advogado()

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
                        cadastro = self.juiz_controler.juiz_dao.get(usuario)
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

        
