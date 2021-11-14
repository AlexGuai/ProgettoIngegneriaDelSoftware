from listaperprenotazioni.Listaperprenotazioni import Listaperprenotazioni


class ControlloreListaPerPrenotazioni():
    def __init__(self):
        super(ControlloreListaPerPrenotazioni, self).__init__()
        self.elimina_callback = None
        self.model = Listaperprenotazioni()
        if os.path.isfile('listaperprenotazioni/data/lista_prenotazione_salvata.pickle'):
            print('esiste')
            with open('listaperprenotazioni/data/lista_prenotazione_salvata.pickle', 'rb') as f:
                lista_perprenotazioni_salvata = pickle.load(f)
            self.model = lista__salvata

    def aggiungi_prenotazione(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)
        with open('listaperprenotazioni/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_perprenotazioni(self):
        return self.model.get_lista_perprenotazioni()

    def get_prenotazioni_by_index(self, index):
        return self.model.get_prenotazioni_by_index(index)

    def rimuovi_prenotazione(self, id):
        self.model.rimuovi_prenotazione(id)
        with open('listaperprenotazioni/data/lista_perprenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('listaperprenotazioni/data/lista_perprenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
