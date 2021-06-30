from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem

from cliente.controllore.ControlloreCliente import ControlloreCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__()
        self.controller = ControlloreCliente(cliente)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)