from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from cliente.model.Cliente import Cliente

"""
class VistaInserisciCliente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciCliente, self).__init__()
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

        v_layout.addWidget(QLabel("Email"))
        self.text_email = QLineEdit(self)
        v_layout.addWidget(self.text_email)

        v_layout.addWidget(QLabel("Telefono"))
        self.text_telefono = QLineEdit(self)
        v_layout.addWidget(self.text_telefono)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_cliente)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Cliente')
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class VistaInserisciCliente(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(266, 628)
        Form.setStyleSheet(
            "QWidget#Form {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(255, 255, 255, 0));};\n"
            "\n"
            "\n"
            "")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.add_cliente)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "Cognome"))
        self.label_3.setText(_translate("Form", "Data di Nascita"))
        self.label_4.setText(_translate("Form", "E-mail"))
        self.label_5.setText(_translate("Form", "Telefono"))
        self.pushButton.setText(_translate("Form", "CONFERMA"))


    def add_cliente(self):
        #id = self.text_id.text()
        nome = self.lineEdit.text()
        cognome = self.lineEdit_2.text()
        datadinascita = self.dateEdit.text()
        email = self.lineEdit_3.text()
        telefono = self.lineEdit_4.text()
        if(nome == ""
                or cognome == ""
                or datadinascita == ""
                or email == ""
                or telefono == ""):
            QMessageBox.critical(None,
                                 'Errore',
                                 "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            self.setupUi.aggiungi_cliente(Cliente((nome+cognome).lower(),
                                                     nome,
                                                     cognome,
                                                     datadinascita,
                                                     email,
                                                     telefono))
            self.callback()
            self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = VistaInserisciCliente()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())