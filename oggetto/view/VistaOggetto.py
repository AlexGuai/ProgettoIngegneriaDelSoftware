from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaOggetto(QWidget):
    def __init__(self, oggetto, rimuovi_cliente, elimina_callback, parent=None):
        super(VistaOggetto, self).__init__()
        self.controller = ControlloreCliente(cliente)
        self.rimuovi_cliente = rimuovi_cliente
        self.elimina_callback = elimina_callback

