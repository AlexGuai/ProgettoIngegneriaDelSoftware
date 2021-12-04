from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaoggettipersi.views.VistaListaOggettiPersi import VistaListaOggettiPersi
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaservizi.views.VistaListaServizi import VistaListaServizi


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Lista Servizi", self.go_lista_servizi), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Oggetti Smarriti", self.go_lista_oggetti_smarriti), 2, 0)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore Piscina Comunale")
    '''
    questa funzione restituisce un bottone generico dato il titolo
    '''
    def get_generic_button(self, titolo, on_click=None):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_lista_oggetti_smarriti(self):
        self.vista_oggetti_persi = VistaListaOggettiPersi()
        self.vista_oggetti_persi.show()
