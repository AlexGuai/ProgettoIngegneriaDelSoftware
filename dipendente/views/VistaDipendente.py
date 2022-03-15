from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from dipendente.controllore.ControlloreDipendente import ControlloreDipendente


class VistaDipendente(QWidget):

    def __init__(self, dipendente, rimuovi_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = ControlloreDipendente(dipendente)
        self.rimuovi_dipendente = rimuovi_dipendente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        font_nome = label_nome.font()
        font_nome.setPointSize(25)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("DATA DI NASCITA: {}".format(self.controller.get_datanascita_dipendente())))
        v_layout.addWidget(self.get_info("LUOGO DI NASCITA: {}".format(self.controller.get_luogonascita_dipendente())))
        v_layout.addWidget(self.get_info("E-MAIL: {}".format(self.controller.get_email_dipendente())))
        v_layout.addWidget(self.get_info("TELEFONO: {}".format(self.controller.get_telefono_dipendente())))
        v_layout.addWidget(self.get_info("LICENZA: {}".format(self.controller.get_licenza_dipendente())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_dipendente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle(self.controller.get_nome_dipendente())

    @staticmethod
    def get_info(text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente_click(self):
        self.rimuovi_dipendente(self.controller.get_nome_dipendente())
        self.elimina_callback()
        self.close()
