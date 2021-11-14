from prenotazione.model.Dipendente import prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("id"))
        self.text_id = QLineEdit(self)
        v_layout.addWidget(self.text_id)

        v_layout.addWidget(QLabel("ora"))
        self.text_ora = QLineEdit(self)
        v_layout.addWidget(self.text_ora)

        v_layout.addWidget(QLabel("corso"))
        self.text_corso = QLineEdit(self)
        v_layout.addWidget(self.text_corso)


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def add_presentazione(self):

        id = self.text_id.text()
        ora = self.text_ora.text()
        corso = self.text_corso.text()

        if (id == ""
                or ora == ""
                or corso == "" ):
            QMessageBox.critical(self,
                                 'Errore',
                                 "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            self.controller.aggiungi_prentazione(Prenotazione(id.lower(),
                                                           ora,
                                                           corso,))
            self.callback()
            self.close()
