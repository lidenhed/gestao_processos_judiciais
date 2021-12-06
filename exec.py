import PySimpleGUI as psg
from interface.execucao import InterfaceSistema
from controllers.execucao import ControladorSistema
controller = ControladorSistema()
inicializar = InterfaceSistema(controller)

inicializar.tela_inicial()