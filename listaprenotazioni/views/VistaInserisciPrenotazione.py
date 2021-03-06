import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSizePolicy, QSpacerItem, QPushButton, QMessageBox, \
    QComboBox

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Data (dd/mm/yyyy)"))
        self.text_data = QLineEdit(self)
        v_layout.addWidget(self.text_data)

        self.combo_clienti = QComboBox()
        self.comboclienti_model = QStandardItemModel(self.combo_clienti)
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti_salvata = pickle.load(f)
            self.lista_clienti_abbonati = [c for c in self.lista_clienti_salvata.get_lista_clienti()]
            for cliente in self.lista_clienti_abbonati:
                item = QStandardItem()
                item.setText(cliente.nome + " " + cliente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboclienti_model.appendRow(item)
            self.combo_clienti.setModel(self.comboclienti_model)
        v_layout.addWidget(QLabel("Cliente"))
        v_layout.addWidget(self.combo_clienti)

        self.combo_servizi = QComboBox()
        self.comboservizi_model = QStandardItemModel(self.combo_servizi)
        if os.path.isfile('listaservizi/data/lista_servizi_salvata.pickle'):
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'rb') as t:
                self.lista_servizi_salvata = pickle.load(t)
            self.lista_servizi_disponibili = [s for s in self.lista_servizi_salvata]
            for servizio in self.lista_servizi_salvata:
                item = QStandardItem()
                item.setText(servizio.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboservizi_model.appendRow(item)
            self.combo_servizi.setModel(self.comboservizi_model)
        v_layout.addWidget(QLabel("Servizio"))
        v_layout.addWidget(self.combo_servizi)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Ok")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle("Nuova Prenotazione")

    def add_prenotazione(self):
        data = self.text_data.text()
        cliente = self.lista_clienti_abbonati[self.combo_clienti.currentIndex()]
        servizio = self.lista_servizi_salvata[self.combo_servizi.currentIndex()]
        if data == "":
            QMessageBox.critical(self, 'Errore',
                                 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(
                Prenotazione((cliente.cognome + cliente.nome), cliente, servizio, data))
            servizio.prenota()
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as handle:
                pickle.dump(self.lista_servizi_salvata, handle, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()
