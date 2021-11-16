from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSizePolicy, QSpacerItem, QPushButton, QMessageBox

from dipendente.model.Dipendente import Dipendente


class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Cognome"))
        self.text_cognome = QLineEdit(self)
        v_layout.addWidget(self.text_cognome)

        v_layout.addWidget(QLabel("Data Di Nascita"))
        self.text_datadinascita = QLineEdit(self)
        v_layout.addWidget(self.text_datadinascita)

        v_layout.addWidget(QLabel("Luogo Di Nascita"))
        self.text_luogodinascita = QLineEdit(self)
        v_layout.addWidget(self.text_luogodinascita)

        v_layout.addWidget(QLabel("Email"))
        self.text_email = QLineEdit(self)
        v_layout.addWidget(self.text_email)

        v_layout.addWidget(QLabel("Telefono"))
        self.text_telefono = QLineEdit(self)
        v_layout.addWidget(self.text_telefono)

        v_layout.addWidget(QLabel("Licenza"))
        self.text_licenza = QLineEdit(self)
        v_layout.addWidget(self.text_licenza)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_dipendente)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Dipendente')

    def add_dipendente(self):
        # id = self.text_id.text()
        nome = self.text_nome.text()
        cognome = self.text_cognome.text()
        datadinascita = self.text_datadinascita.text()
        luogodinascita = self.text_luogodinascita.text()
        email = self.text_email.text()
        telefono = self.text_telefono.text()
        licenza = self.text_licenza.text()
        if (nome == ""
                or cognome == ""
                or datadinascita == ""
                or luogodinascita == ""
                or email == ""
                or telefono == ""
                or licenza == ""):
            QMessageBox.critical(self,
                                 'Errore',
                                 "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            self.controller.aggiungi_dipendente(Dipendente(nome,
                                                           cognome,
                                                           datadinascita,
                                                           luogodinascita,
                                                           email,
                                                           telefono,
                                                           licenza
                                                           ))
            self.callback()
            self.close()
