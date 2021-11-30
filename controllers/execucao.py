from controllers.juiz import JuizController

class ControladorSistema:
    def __init__(self):
        self.__juizControler = JuizController(self)

    def init_module_juiz(self):
        self.__juizControler.cadastrar_juiz()