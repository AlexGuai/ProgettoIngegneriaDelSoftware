class Dipendente():
    def __init__(self,  nome, cognome, datanascita, luogonascita,  telefono, email, licenza):
        super(Dipendente, self).__init__()
        self.nome = nome
        self.cognome = cognome
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.telefono = telefono
        self.email = email
        self.licenza = licenza
