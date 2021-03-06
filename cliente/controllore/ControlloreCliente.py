class ControlloreCliente():
    def __init__(self, cliente):
        self.model = cliente

    def get_id_cliente(self):
        return self.model.id

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_datadinascita_cliente(self):
        return self.model.datadinascita

    def get_email_cliente(self):
        return self.model.email

    def get_telfono_cliente(self):
        return self.model.telefono

    def get_abbonamento_cliente(self):
        return self.model.abbonamento

    def aggiungi_nuovo_abbonamento_cliente(self, abbonamento):
        self.model.add_abbonamento(abbonamento)
