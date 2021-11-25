import self as self


class ListaOggettiPersi():
    def __init__(self):
        super(ListaOggettiPersi, self).__init__()
        self.lista_oggettipersi= []

    def aggiungi_oggettoperso(self, oggetto):
        self.lista_oggettipersi.append(oggetto)

    def rimuovi_oggettoritrovato(self, nome):
        def is_selected_oggettoritrovato(oggetto):
            if oggetto.nome  == nome
                return True
            return False
      self.lista_oggettipersi.remove(list(filter(is_selected_oggettoritrovato , self.lista_oggettipersi))[0])

    def get_oggetti_by_index(self, index):
        return self.lista_oggettipersi[index]

    def get_lista_oggettipersi(self):
        return self.lista_oggettipersi