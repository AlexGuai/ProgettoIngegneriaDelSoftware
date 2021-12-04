class Oggetto():
    def __init__(self, tipo, nome, descrizione, dataRitrovamento) -> object:
        super(Oggetto, self).__init__()
        self.tipo = tipo
        self.nome = nome
        self.descrizione = descrizione
        self.dataRitrovamento = dataRitrovamento


