class ControlloreOggetto():
    def __init__(self, oggetto):
        self.model = oggetto

    def get_tipo_oggetto(self):
        return self.model.tipo

    def get_nome_oggetto(self):
        return self.model.nome

    def get_descrizione_oggetto(self):
        return self.model.descrizione

    def get_data_ritrovamento_oggetto(self):
        return self.model.dataRitrovamento




