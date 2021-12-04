from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from oggetto.model.Oggetto import Oggetto


class VistaInserisciOggetto(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciOggetto, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Tipo"))
        self.text_tipo = QLineEdit(self)
        v_layout.addWidget(self.text_tipo)

        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Descrizione"))
        self.text_descrizione = QLineEdit(self)
        v_layout.addWidget(self.text_descrizione)

        v_layout.addWidget(QLabel("Data Ritrovamento"))
        self.text_dataRitrovamento = QLineEdit(self)
        v_layout.addWidget(self.text_dataRitrovamento)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_oggetto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Oggetto')

    def add_oggetto(self):
        tipo = self.text_tipo.text()
        nome = self.text_nome.text()
        descrizione = self.text_descrizione.text()
        dataRitrovamento = self.text_dataRitrovamento.text()
        if(tipo == ""
                or nome == ""
                or descrizione == ""
                or dataRitrovamento == ""):
            QMessageBox.critical(self,
                                 'Errore',
                                 "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            self.controller.aggiungi_oggetto(Oggetto(tipo,
                                                     nome,
                                                     descrizione,
                                                     dataRitrovamento))
            self.callback()
            self.close()
