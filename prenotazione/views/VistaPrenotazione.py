from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from prenotazione.controllore.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__()
        self.controller = ControllorePrenotazione(prenotazione)
        self.disdici_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_servizio_prenotazione().nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(25)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cf = QLabel("Cliente: {}".format(self.controller.get_cliente_prenotazione().nome + " " + self.controller.get_cliente_prenotazione().cognome))
        font_cf = label_cf.font()
        font_cf.setPointSize(25)
        label_cf.setFont(font_cf)
        v_layout.addWidget(label_cf)

        label_datanascita = QLabel("Data: {}".format(self.controller.get_data_prenotazione()))
        font_datanascita = label_datanascita.font()
        font_datanascita.setPointSize(25)
        label_datanascita.setFont(font_datanascita)
        v_layout.addWidget(label_datanascita)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_disdici = QPushButton("Disdici")
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.resize(600, 300)

    def disdici_prenotazione_click(self):
        self.disdici_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()
