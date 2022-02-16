import PySimpleGUI as psg


class InterfaceAdvogado:

    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None

    def tela_cadastrar_Advogado(self, cpf):
        while True:
            layout_cadastro = [
                [psg.Text('Preencha os dados abaixo:')],
                [psg.Text('Nome:', size=(20, 1)), psg.InputText('', key='nome')],
                [psg.Text('Código OAB:', size=(20, 1)), psg.InputText('', key='cod_OAB')],
                [psg.Text(f'Login:                                  {cpf}')],
                [psg.Text('Senha:', size=(20, 1)), psg.InputText('', key='password', password_char='*')],
                [psg.Button('Enviar Dados'), psg.Button('Voltar')]
            ]
            tela_cadastro = psg.Window('Cadastrar Advogado').Layout(layout_cadastro)
            event, values = tela_cadastro.Read()
            tela_cadastro.Close()
            if event == 'Voltar' or event == psg.WIN_CLOSED:
                break
            else:
                return values

    def get_informacao(self, msg_cabecalho, msg_corpo):
        layout_info = [
            [psg.Text(msg_corpo, size=(30, 1)), psg.InputText('')],
            [psg.Button('Remover'), psg.Button('Voltar')]
        ]
        tela_get_info = psg.Window(msg_cabecalho).Layout(layout_info)
        button, values = tela_get_info.Read()
        tela_get_info.Close()
        return button, values[0]

    def aviso(self, msg):
        layout_aviso = [
            [psg.Text(msg)],
            [psg.Ok()]
        ]
        tela_aviso = psg.Window('Aviso').Layout(layout_aviso)
        tela_aviso.Read()
        tela_aviso.Close()
