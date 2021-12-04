from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QLabel, \
    QSpacerItem

from oggetto.controllore.ControlloreOggetto import ControlloreOggetto


class VistaOggetto(QWidget):
    def __init__(self, oggetto, rimuovi_oggetto, elimina_callback, parent=None):
        super(VistaOggetto, self).__init__()
        self.controller = ControlloreOggetto(oggetto)
        self.rimuovi_oggetto = rimuovi_oggetto
        self.elimina_callback = elimina_callback


        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_oggetto())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("tipo", self.controller.get_tipo_oggetto()))
        v_layout.addWidget(self.get_label_info("nome", self.controller.get_nome_oggetto()))
        v_layout.addWidget(self.get_label_info("descrizione", self.controller.get_descrizione_oggetto()))
        v_layout.addWidget(self.get_label_info("dataRitrovamento", self.controller.get_data_ritrovamento_oggetto()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_oggetto_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_tipo_oggetto() + " " + self.controller.get_nome_oggetto())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def elimina_oggetto_click(self):
        self.rimuovi_oggetto(self.controller.get_nome_oggetto())
        self.elimina_callback()
        self.close()
