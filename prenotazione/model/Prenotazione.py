class Prenotazione():
    def __init__(self,id, cliente, servizio, data):
        super(Prenotazione, self).__init__()
        self.id = id
        self.cliente = cliente
        self.servizio = servizio
        self.data = data
