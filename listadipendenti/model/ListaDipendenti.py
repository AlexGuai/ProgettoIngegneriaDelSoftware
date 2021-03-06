class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def rimuovi_dipendente(self, nome):
        for dipendente in self.lista_dipendenti:
            if dipendente.nome == nome:
                self.lista_dipendenti.remove(dipendente)
                return True
        return False

    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    def get_lista_dipendenti(self):
        return self.lista_dipendenti