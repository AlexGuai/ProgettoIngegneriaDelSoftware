class ControlloreOggetto():
    def __init__(self, oggetto):
        self.model = oggetto

    def get_orologio_oggetto(self):
        return self.model.orologio

    def get_telefono_oggetto(self):
        return self.model.telefono

    def get_ciabatte_oggetto(self):
        return self.model.ciabatte




