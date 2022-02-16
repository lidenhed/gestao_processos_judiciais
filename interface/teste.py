import PySimpleGUI as psg

class Teste:
    
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None
        
    def tela_teste(self):
        while True:
            layout_inicia_sistema = [
                [psg.Text('Escolha a opção para teste:')],
                [psg.Radio('Cadastrar Processo     ', "RADIO", size=(20, 1)),
                psg.Radio('Efetuar Ato Processual    ', "RADIO", size=(20, 1)),
                psg.Radio('Despachar    ', "RADIO", size=(15, 1))],
                [psg.Button('Enviar'), psg.Button('Sair')]
            ]
            tela_inicio_sistema = psg.Window(
                'Iniciar ModuloTeste').Layout(layout_inicia_sistema)
            event, values = tela_inicio_sistema.read()
            if event == psg.WIN_CLOSED or event == 'Sair':
                tela_inicio_sistema.Close()
                exit(1)
            else:
                if values[0]:
                    tela_inicio_sistema.Close()
                    self.__controlador.init_module_cadastrar_processo()
                elif values[1]:
                    tela_inicio_sistema.Close()
                    self.__controlador.init_module_efetuar_ato_processual()
                else:
                    tela_inicio_sistema.Close()
                    self.__controlador.init_module_despachar()
                    