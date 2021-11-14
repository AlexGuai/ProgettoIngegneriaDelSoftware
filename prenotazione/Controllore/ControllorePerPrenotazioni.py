class ControllorePerPrenotazioni:

    def __init__(self, prenotazioni):
        self.prenotazioni = prenotazioni
        self.model = prenotazioni

    def get_id_prenotazione(self):
        return self.model.id

    def get_ora_prenotazione(self):
        return self.model.ora

    def get_corso_prenotazione(self):
        return self.model.corso