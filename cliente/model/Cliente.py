class Cliente():
    def __init__(self, id, nome, cognome, datadinascita, email, telefono):
        super(Cliente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.datadinascita = datadinascita
        self.email = email
        self.telefono = telefono
        self.abbonamento = None

    def add_abbonamento(self, abbonamento):
        self.abbonamento = abbonamento

    def get_abbonamento(self):
        if self.abbonamento.is_scaduto():
            self.abbonamento = None
            return None
        else:
            return self.abbonamento