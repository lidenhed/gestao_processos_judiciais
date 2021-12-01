import PySimpleGUI as psg
from enum import Enum
from controllers.execucao import ControladorSistema


class Modulo(Enum):
    JUIZ = 1
    ADVOGADO = 2
    PARTE = 3


class Execucao:
    def __init__(self, modulo):
        self.__modulo = modulo


psg.theme('Reddit')
layout = [[psg.Text('Carregando...', font='ANY 13', pad=(100, 10))],
          [psg.Button('Cancelar')]]

window = psg.Window('Sistema de Gestão de Processos Judiciais').Layout(layout)

interromper_programa = False
count = 0
while count < 150:
    count = count + 1
    event, values = window.Read(timeout=5)
    if event in (None, 'Exit', 'Cancelar'):
        interromper_programa = True
        break
window.Close()

if __name__ == "__main__":
    if interromper_programa:
        exit(2)
    while True:
        layout_inicia_sistema = [
            [psg.Text('Efetuar Login como:')],
            [psg.Radio('Juiz     ', "RADIO", size=(10, 1)),
             psg.Radio('Advogado    ', "RADIO", size=(10, 1)),
             psg.Radio('Parte    ', "RADIO", size=(10, 1))],
            [psg.Button('Enviar'), psg.Button('Sair')]
        ]
        tela_inicio_sistema = psg.Window(
            'Iniciar Modulo').Layout(layout_inicia_sistema)
        event, values = tela_inicio_sistema.read()
        if event == psg.WIN_CLOSED or event == 'Sair':
            tela_inicio_sistema.Close()
            exit(1)
        else:
            if values[0]:
                Execucao(Modulo.JUIZ)
                tela_inicio_sistema.Close()
                ControladorSistema().init_module_juiz()
            elif values[1]:
                Execucao(Modulo.ADVOGADO)
                tela_inicio_sistema.Close()
                # ControladorSistema().inicia_module_advogado()
            else:
                Execucao(Modulo.PARTE)
                tela_inicio_sistema.Close()
                ControladorSistema().init_module_parte()
