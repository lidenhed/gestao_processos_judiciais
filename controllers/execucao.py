from controllers.juiz import JuizController
from controllers.parte import ParteController

class ControladorSistema:
    def __init__(self):
        self.__juizControler = JuizController(self)
        self.__parteController = ParteController(self)

    def init_module_juiz(self):
        self.__juizControler.cadastrar_juiz()

    def init_module_parte(self):
        self.__parteController.cadastrar_parte()
