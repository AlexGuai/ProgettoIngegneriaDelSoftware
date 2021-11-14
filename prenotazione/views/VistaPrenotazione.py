from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton


import prenotazione.controllore.ControllorePerPrenotazioni



class VistaPrenotazione (QWidget):

    def __init__(self, prenotazioni , rimuovi_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControlloreListaperprenotazioni(prenotazioni)
        self.rimuovi_prenotazione = rimuovi_prenotazione
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_id = QLabel(self.controller.get_id_prenotazione() + " " + self.controller.get_id_prenotazione())
        font_id = label_id.font()
        font_id.setPointSize(30)
        label_id.setFont(font_id)
        v_layout.addWidget(label_id)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("id: {}".format(self.controller.get_id_prenotazione())))
        v_layout.addWidget(self.get_info("ora: {}".format(self.controller.get_ora_prenotazione())))
        v_layout.addWidget(self.get_info("corso: {}".format(self.controller.get_corso_prenotazione())))


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_id_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_id_prenotazione())


def elimina_prenotazione_click(self):
        self.rimuovi_dipendente(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()
