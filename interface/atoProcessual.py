import PySimpleGUI as psg

class InterfaceAtoProcessual:

    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None
            
    def tela_realizar_ato(self):
        settings = psg.UserSettings()
        psg.user_settings_filename(path='.')
        while True:
            layout_ato_processual = [
                [psg.Text('Preencha os campos abaixo:', size=(30, 1))],
                [psg.Text('', size=(30, 1))],
                [psg.Checkbox('Solicitar urgência:     ',"CHECKBOX", size=(30, 1))],
                [psg.Text('Anexe aqui seu arquivo:', size=(30, 1))],
                [psg.Input(psg.user_settings_get_entry('-filename-', ''), key='-IN-'), psg.FileBrowse()],
                [psg.Button('Enviar'), psg.Button('Voltar')]
            ]
            tela_realizar_ato = psg.Window('Tela Realizar Ato').Layout(layout_ato_processual)
            event, values = tela_realizar_ato.Read()
            tela_realizar_ato.Close()
            if event == 'Voltar' or event == psg.WIN_CLOSED:
                break
            else:
                settings['-filename-'] = values['-IN-']
                return values
                
    def aviso(self, msg):
        layout_aviso = [
            [psg.Text(msg)],
            [psg.Ok()]
        ]
        tela_aviso = psg.Window('Aviso').Layout(layout_aviso)
        tela_aviso.Read()
        tela_aviso.Close()