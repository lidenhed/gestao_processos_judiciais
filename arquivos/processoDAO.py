import pickle
from entities.processo import Processo

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
            data = 'metodoquepegadataaqui'
            novo_processo = Processo(cod_OAB, cpf_autor, data, eh_sigiloso, id_processo, cpf_reu, id_juiz, anexos)
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

    def add_anexo(self):
        return False

    def add_data(self):
        return False

    def set_urgencia(self):
        return False




        






            
