from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QListView, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from cliente.view.VistaCliente import VistaCliente
from listaclienti.controllore.ControlloreListaClienti import ControlloreListaClienti
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
from GUI.immaginiprogetto import immagini_rc

class VistaListaClienti(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(868, 628)
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"    background-image: url(:/piscina1/MicrosoftTeams-image.png);\n"
"}")

        self.controller = ControlloreListaClienti()

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.show_selected_info)
        self.pushButton_2.clicked.connect(self.show_new_cliente)
        self.update_ui()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "VISUALIZZA CLIENTE"))
        self.pushButton_2.setText(_translate("Form", "NUOVO CLIENTE"))


    def show_selected_info(self):
        try:
            selected = self.listView.selectedIndexes()[0].row()
            cliente_selezionato = self.controller.get_cliente_by_index(selected)
            self.vista_cliente = VistaCliente(cliente_selezionato, self.controller.rimuovi_cliente, self.update_ui)
            self.vista_cliente.show()
        except:
            QMessageBox.critical(None,
                                 'Errore',
                                 'Nessun cliente selezionato.',
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)

    def show_new_cliente(self):
        self.window = QtWidgets.QWidget()
        self.vista_inserisci_cliente = VistaInserisciCliente()
        self.vista_inserisci_cliente.setupUi(self.window)
        self.window.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.listView)
        for cliente in self.controller.get_lista_dei_clienti():
            item = QStandardItem()
            item.setText(cliente.nome+" "+cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)



    def closeEvent(self, event):
        self.controller.save_data()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = VistaListaClienti()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())