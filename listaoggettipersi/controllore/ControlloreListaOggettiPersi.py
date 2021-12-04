import pickle
import os.path

from listaoggettipersi.model.ListaOggettiPersi import ListaOggettiPersi


class ControlloreListaOggettiPersi():
    def __init__(self):
        super(ControlloreListaOggettiPersi, self).__init__()
        self.model = ListaOggettiPersi()
        if os.path.isfile('listaoggettipersi/data/lista_oggetti_persi_salvata.pickle'):
            print("esiste")
            with open('listaoggettipersi/data/lista_oggetti_persi_salvata.pickle', 'rb') as f:
                lista_oggetti_persi_salvata = pickle.load(f)
            self.model = lista_oggetti_persi_salvata

    def aggiungi_oggetto(self, oggetto):
        self.model.aggiungi_oggetto_perso(oggetto)
        with open('listaoggettipersi/data/lista_oggetti_persi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_degli_oggetti_persi(self):
        return self.model.get_lista_oggetti_persi()

    def get_oggetto_by_index(self, index):
        return self.model.get_oggetto_by_index(index)

    def rimuovi_oggetto(self, nome):
        self.model.rimuovi_oggetto(nome)
        with open('listaoggettipersi/data/lista_oggetti_persi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('listaoggettipersi/data/lista_oggetti_persi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
