from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QPushButton

from abbonamento.views.VistaAbbonamento import VistaAbbonamento
from cliente.controllore.ControlloreCliente import ControlloreCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, rimuovi_cliente, elimina_callback, parent=None):
        super(VistaCliente, self).__init__()
        self.controller = ControlloreCliente(cliente)
        self.rimuovi_cliente = rimuovi_cliente
        self.elimina_callback = elimina_callback

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("nome", self.controller.get_nome_cliente()))
        v_layout.addWidget(self.get_label_info("cognome", self.controller.get_cognome_cliente()))
        v_layout.addWidget(self.get_label_info("datadinascita", self.controller.get_datadinascita_cliente()))
        v_layout.addWidget(self.get_label_info("email", self.controller.get_email_cliente()))
        v_layout.addWidget(self.get_label_info("telefono", self.controller.get_telfono_cliente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_abbonamento = QPushButton("Abbonamento")
        btn_abbonamento.clicked.connect(self.check_abbonamento)
        v_layout.addWidget(btn_abbonamento)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_cliente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def check_abbonamento(self):
        self.vista_abbonamento = VistaAbbonamento(self.controller.get_abbonamento_cliente(),
                                                  self.controller.aggiungi_nuovo_abbonamento_cliente)
        self.vista_abbonamento.show()

    def elimina_cliente_click(self):
        self.rimuovi_cliente(self.controller.get_nome_cliente())
        self.elimina_callback()
        self.close()