from interface.validadorCPF import InterfaceValidadorCPF


class ValidadorCPF:

    def __init__(self):
        self.__tela_validador = InterfaceValidadorCPF(self)

    def valida_cpf(self, numbers):
        cpf = [int(char) for char in numbers if char.isdigit()]

        if len(cpf) != 11:
            return False

        if cpf == cpf[::-1]:
            return False

        for i in range(9, 11):
            value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != cpf[i]:
                return False
        return True

    def solicita_cpf_cadastro(self):
        while True:
            cpf = self.__tela_validador.abre_tela()
            if cpf is None:
                return cpf
            else:
                cpf = cpf[0]
                cpf_eh_valido = self.valida_cpf(cpf)
                if cpf_eh_valido:
                    return cpf
                else:
                    self.__tela_validador.tela_aviso('CPF inválido')

    def solicita_cpf_busca(self):
        cpf = self.__tela_validador.abre_tela()
        if cpf is None:
            return cpf
        else:
            cpf = cpf[0]
            return cpf
