import pickle
import os.path

from listaoggettipersi.model.ListaOggettiPersi import ListaOggettiPersi


class ControlloreListaOggettiPersi():
    def __init__(self):
        super(ControlloreListaOggettiPersi, self).__init__()
        self.model = ListaOggettiPersi()
        if os.path.isfile('listaoggettipersi/data/lista_clienti_salvata.pickle'):
            print("esiste")
            with open('listaclienti/data/lista_oggettipersi_salvata.pickle', 'rb') as f:
                lista_oggettipersi_salvata = pickle.load(f)
            self.model = lista_oggettipersi_salvata

    def aggiungi_oggetto(self, oggetto):
        self.model.aggiungi_oggetto(oggetto)
        with open('listaggettipersi/data/lista_oggettipersi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_oggetti_persi(self):
        return self.model.get_lista_oggettipersi()

    def get_oggetto_by_index(self, index):
        return self.model.get_oggetto_by_index(index)

    def rimuovi_oggettoritrovato(self, nome):
        self.model.rimuovi_oggettoritrovato(nome)
        with open('listapggettipersi/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('listaoggettipers/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)