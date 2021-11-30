import PySimpleGUI as psg


class InterfaceValidadorCPF:

    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None
        self.__window_sec = None

    def init_components(self):
        layout = [
            [psg.Text('Insira o CPF (somente digitos):\n\n')],
            [psg.InputText('')],
            [psg.Button('Enviar'), psg.Button('Voltar')]
        ]
        self.__window = psg.Window('Validador CPF').Layout(layout)

    def close_tela(self):
        self.__window.Close()

    def abre_tela(self):
        self.init_components()
        evento, cpf = self.__window.Read()
        self.close_tela()
        if evento == 'Voltar' or evento == psg.WIN_CLOSED:
            return None
        else:
            return cpf

    def tela_aviso(self, mpsg_erro):
        layout1 = [
            [psg.Text(mpsg_erro)],
            [psg.Ok()]
        ]
        tela_aviso = psg.Window('Erro').Layout(layout1)
        tela_aviso.Read()
        tela_aviso.Close()
