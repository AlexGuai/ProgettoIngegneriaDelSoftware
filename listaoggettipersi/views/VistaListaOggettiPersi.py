from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QListView, QPushButton

from oggetto.view.VistaOggetto import VistaOggetto
from listaoggettipersi.controllore.ControlloreListaOggettiPersi import ControlloreListaOggettiPersi
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
import self

class VistaListaOggettiPersi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaOggettiPersi self).__init__(parent)

        self.controller = ControlloreListaOggettiPersi()

        h_layout = QHBoxLayout()

        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo oggetto")
        new_button.clicked.connect(self.show_new_oggetto)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista oggetti persi')

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
       oggeto_selezionato = self.controller.get_oggetto_by_index(selected)
        self.vista_oggetto = VistaOggetto(vista_selezionato, self.controller.rimuovi_oggettoritrovato, self.update_ui)
        self.vista_cliente.show()

    def show_new_oggetto(self):
        self.vista_inserisci_oggetto= VistaInserisciCliente (self.controller, self.update_ui)
        self.vista_inserisci_oggetto.show()



    def closeEvent(self, event):
        self.controller.save_data()