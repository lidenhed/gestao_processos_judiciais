from interface.validadorCPF import InterfaceValidadorCPF


class ValidadorCPF:

    def __init__(self):
        self.__tela_validador = InterfaceValidadorCPF(self)

    def valida_cpf(self, cpf):
        try:
            if len(cpf) < 11:
                return False

            if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
                return False

            calc = lambda t: int(t[1]) * (t[0] + 2)
            d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
            d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
            return str(d1) == cpf[-2] and str(d2) == cpf[-1]
        except TypeError:
            pass
        except ValueError:
            return False

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
