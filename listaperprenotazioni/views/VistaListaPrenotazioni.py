from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

import prenotazione.views.VistaPrenotazione
from listaperprenotazioni.controllore.ControlloreListaPerPrenotazioni import ControlloreListaPerPrenotazioni
from listaperprenotazioni.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione


class VistaListaPrenotazione(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPrenotazione, self).__init__(parent)

        self.controller = ControlloreListaPerPrenotazioni()

        h_layout = QHBoxLayout()

        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_prenotazioni)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Prenotazione')

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        cliente_selezionato = self.controller.get_dipendente_by_index(selected)
        self.vista_prenotazione= prenotazione.views.VistaPrenotazione.VistaPrenotazione(cliente_selezionato, self.controller.rimuovi_prenotazione(),
                                                                                        self.update_ui)
        self.vista_prenotazione.show()

    def show_new_prenotazione(self):
        self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller, self.update_ui)
        self.vista_inserisci_prenotazione.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for presentazione in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            assert isinstance(presentazione.id)
            item.setText(presentazione.id)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()