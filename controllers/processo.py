from interface.processo import InterfaceProcesso
from arquivos.processoDAO import ProcessoDAO
from controllers.validadorCPF import ValidadorCPF

class ProcessoController:

    def __init__(self, controlador_execucao):
        self.__interface_processo = InterfaceProcesso(self)
        self.__processo_dao = ProcessoDAO()
        self.__controlador_execucao = controlador_execucao
        

    def cadastrar_processo(self):
        while True:
            valores = self.__interface_processo.tela_cadastrar_processo()
            cadastro_ok = self.verifica_cadastro_completo(valores)
            if cadastro_ok:
                parte_controller = self.__controlador_execucao.parte_controller()
                advogado_controller = self.__controlador_execucao.advogado_controller()
                juiz_controller = self.__controlador_execucao.juiz_controller()
                validador_cpf = self.__controlador_execucao.validadorCPF()
                cod_OAB = valores[0]
                cpf_autor = valores[1]
                eh_sigiloso = valores[2]
                cpf_reu = valores[4]
                anexo = valores[5]
                advogado_encontrado = advogado_controller.verifica_cod_OAB(cod_OAB)
                if advogado_encontrado:
                    cpf_valido_autor = validador_cpf.valida_cpf(cpf_autor)
                    if cpf_valido_autor:
                        cpf_encontrado_autor = parte_controller.verifica_cpf_jah_existente(cpf_autor)
                        if cpf_encontrado_autor:
                            cpf_valido_reu = validador_cpf.valida_cpf(cpf_reu)
                            if cpf_valido_reu:
                                arquivo_anexado = self.verifica_anexo(anexo)
                                if arquivo_anexado:
                                    id_processo = self.atribui_id()
                                    self.solicita_sigilo(eh_sigiloso)
                                    id_juiz = juiz_controller.sortear_juiz()
                                    sucesso_add = self.__processo_dao.add(cod_OAB, cpf_autor, eh_sigiloso, cpf_reu, anexo, id_juiz, id_processo)
                                    if sucesso_add:
                                        self.__interface_juiz.aviso('Processo cadastrado com sucesso')
                                else:
                                    self.__interface_processo.aviso('Anexe um arquivo')
                                    continue
                            else:
                                self.__interface_processo.aviso('CPF do réu inválido')
                                continue
                        else:
                            self.__interface_processo.aviso('CPF não cadastrado')
                            continue
                                    
                    else:
                        self.__interface_processo.aviso('CPF do autor inválido')
                        continue
                else:
                    self.__interface_processo.aviso('Advogado não encontrado')
                    continue                  
            break
    
    def atribui_id(self):
        return 'oi'
        
    def realizar_ato_processual(self): ##colocar id processo no parametro
        valores = self.__interface_processo.tela_realizar_ato()
        
        arquivo_anexado = self.verifica_anexo(nome_anexo)
        return False
    
    def despachar(self, id_processo):
        return False
    
    def verifica_anexo(self, nome_anexo):
        if nome_anexo == '':
            return False
        if nome_anexo.split('.') == Null:
            return False
        return True
        
    def verifica_cadastro_completo(self, values):
        if values['anexos'] == '' or values['autor'] == '' or values['codOAB_advogado_autor'] == '' or values['eh_sigiloso'] == '' or values['reu'] == '':
            self.__interface_processo.close_tela_principal()
            return False
        return True
