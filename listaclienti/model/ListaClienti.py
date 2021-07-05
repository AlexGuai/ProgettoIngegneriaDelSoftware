class ListaClienti():
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def rimuovi_cliente(self, nome):
        def is_selected_cliente(cliente):
            if cliente.nome == nome:
                return True
            return False
        self.lista_clienti.remove(list(filter(is_selected_cliente, self.lista_clienti))[0])

    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    def get_lista_clienti(self):
        return self.lista_clienti