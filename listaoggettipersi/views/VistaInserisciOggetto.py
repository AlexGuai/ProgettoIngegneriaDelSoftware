from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from oggetto.model.Oggetto import Oggetto


class VistaInserisciOggetto(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciOggetto, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel(""))
        self.text_nome = QLineEdit(self)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Orologio"))
        self.text_cognome = QLineEdit(self)
        v_layout.addWidget(self.text_cognome)

        v_layout.addWidget(QLabel("telefono"))
        self.text_datadinascita = QLineEdit(self)
        v_layout.addWidget(self.text_datadinascita)

        v_layout.addWidget(QLabel("Ciabatte"))
        self.text_email = QLineEdit(self)
        v_layout.addWidget(self.text_email)


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_oggetto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Oggetto')




            self.callback()
            self.close()
