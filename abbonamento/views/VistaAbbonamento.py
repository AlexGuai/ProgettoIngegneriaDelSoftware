from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSizePolicy, QSpacerItem

from abbonamento.controllore.ControlloreAbbonamento import ControlloreAbbonamento
from abbonamento.model.Abbonamento import Abbonamento


class VistaAbbonamento(QWidget):
    def __init__(self, abbonamento, callback_inserisci_abbonamento):
        super(VistaAbbonamento, self).__init__()
        self.controller = ControlloreAbbonamento(abbonamento)
        self.callback_inserisci_abbonamento = callback_inserisci_abbonamento

        v_layout = QVBoxLayout()
        if self.controller.is_abbonato():
            label_data = QLabel(self.controller.get_scadenza_string())
            font_data = label_data.font()
            font_data.setPointSize(25)
            label_data.setFont(font_data)
            v_layout.addWidget(label_data)
        else:
            label_errore = QLabel("Cliente non abbonato")
            font_errore = label_errore.font()
            font_errore.setPointSize(25)
            label_errore.setFont(font_errore)
            v_layout.addWidget(label_errore)
            label_errore1 = QLabel("Scadenza abbonamento(dd/mm/yyyy):")
            font_errore1 = label_errore1.font()
            font_errore1.setPointSize(25)
            label_errore1.setFont(font_errore1)
            v_layout.addWidget(label_errore1)
            self.text_scadenza = QLineEdit()
            v_layout.addWidget(self.text_scadenza)
            btn_inserisci = QPushButton("Aggiungi")
            btn_inserisci.clicked.connect(self.add_abbonamento_click)
            v_layout.addWidget(btn_inserisci)



        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Abbonamento')

    def add_abbonamento_click(self):
        try:
            date = datetime.strptime(self.text_scadenza.text(), '%d/%m/%Y')
            self.callback_inserisci_abbonamento(Abbonamento(date.timestamp()))
            self.close()
        except:
            QMessageBox.critical(self,
                                 'Errore',
                                 'Inserisci la data nel formato richiesto: dd/mm/yyyy',
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
