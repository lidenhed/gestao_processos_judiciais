import pickle
from entities.processo import Processo
from datetime import date

class ProcessoDAO:

    def __init__(self, datasource='processo.pkl'):
        self.datasource = datasource
        self.object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.object_cache, open(self.datasource, 'wb'))

    def __load(self):
        self.object_cache = pickle.load(open(self.datasource, 'rb'))

    def add(cod_OAB, cpf_autor, eh_sigiloso, cpf_reu, anexo, id_juiz, id_processo):
        if (isinstance(anexo, str) and
                isinstance(cpf_autor, str) and
                isinstance(cod_OAB, int) and
                isinstance(eh_sigiloso, bool) and
                isinstance(id_processo, int) and
                isinstance(id_juiz, int) and
                isinstance(cpf_reu, str)):
            data = date.today()
            novo_processo = Processo(cod_OAB, cpf_autor, eh_sigiloso, id_processo, cpf_reu, id_juiz)
            novo_processo.data.setter(data)
            novo_processo.anexos.setter(anexo)
            self.object_cache[novo_processo.id_processo] = novo_processo
            self.__dump()
            return True
        return False

    def get(self, key):
        if isinstance(key, int):
            try:
                return self.object_cache[key]
            except KeyError:
                return None

    def remove(self, key):
        if isinstance(key, int):
            try:
                self.object_cache.pop(key)
                self.__dump()
                return True
            except KeyError:
                return False

    def get_all(self):
        return self.object_cache.values()

    def add_anexo(self, anexo, id_processo):
        processo = self.get(id_processo)
        processo.anexos(anexo)

    def add_data(self, data, id_processo):
        processo = self.get(id_processo)
        processo.data(data)

    def set_urgencia(self, eh_urgente, id_processo):
        processo = self.get(id_processo)
        processo.eh_urgente(eh_urgente)
        
    def set_sigilo(self, eh_sigiloso, id_processo):
        processo = self.get(id_processo)
        processo.eh_sigiloso(eh_sigiloso)




        






            
