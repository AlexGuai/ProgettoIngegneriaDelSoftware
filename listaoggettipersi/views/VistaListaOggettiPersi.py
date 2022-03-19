from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QListView, QPushButton, QMessageBox

from oggetto.view.VistaOggetto import VistaOggetto
from listaoggettipersi.controllore.ControlloreListaOggettiPersi import ControlloreListaOggettiPersi
from listaoggettipersi.views.VistaInserisciOggetto import VistaInserisciOggetto

class VistaListaOggettiPersi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaOggettiPersi, self).__init__(parent)

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
        try:
            selected = self.list_view.selectedIndexes()[0].row()
            oggeto_selezionato = self.controller.get_oggetto_by_index(selected)
            self.vista_oggetto = VistaOggetto(oggeto_selezionato, self.controller.rimuovi_oggetto, self.update_ui)
            self.vista_oggetto.show()
        except:
            QMessageBox.critical(self,
                                 'Errore',
                                 'Nessun oggetto selezionato.',
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)

    def show_new_oggetto(self):
        self.vista_inserisci_oggetto= VistaInserisciOggetto(self.controller, self.update_ui)
        self.vista_inserisci_oggetto.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for oggetto in self.controller.get_lista_degli_oggetti_persi():
            item = QStandardItem()
            item.setText(oggetto.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
