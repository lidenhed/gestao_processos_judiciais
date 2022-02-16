from controllers.execucao import ControladorSistema
from interface.teste import Teste

controller = ControladorSistema()                 
teste = Teste(controller)
teste.tela_teste()