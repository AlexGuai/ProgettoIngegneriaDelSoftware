
class ListaOggettiPersi():
    def __init__(self):
        super(ListaOggettiPersi, self).__init__()
        self.lista_oggetti_persi = []

    def aggiungi_oggetto_perso(self, oggetto):
        self.lista_oggetti_persi.append(oggetto)

    def rimuovi_oggetto_ritrovato(self, nome):
        def is_selected_oggetto_ritrovato(oggetto):
            if oggetto.nome == nome:
                return True
            return False
        self.lista_oggetti_persi.remove(list(filter(is_selected_oggetto_ritrovato, self.lista_oggetti_persi))[0])

    def get_oggetti_by_index(self, index):
        return self.lista_oggetti_persi[index]

    def get_lista_oggettipersi(self):
        return self.lista_oggetti_persi