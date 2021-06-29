class Servizio():

    def __init__(self, id, nome, tipo, posizione):
        super(Servizio, self).__init__()
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.posizione = posizione
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False
