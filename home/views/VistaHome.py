from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaoggettipersi.views.VistaListaOggettiPersi import VistaListaOggettiPersi
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaservizi.views.VistaListaServizi import VistaListaServizi
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.setEnabled(True)
        Home.resize(868, 628)
        Home.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Home.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 210, 181, 31))
        self.pushButton.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 250, 181, 31))
        self.pushButton_2.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 290, 181, 31))
        self.pushButton_3.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 330, 181, 31))
        self.pushButton_4.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 370, 181, 31))
        self.pushButton_5.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\";")
        self.pushButton_5.setObjectName("pushButton_5")
        Home.setCentralWidget(self.centralwidget)

        self.retranslateUi(Home)
        self.pushButton.clicked.connect(self.go_lista_clienti)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "MainWindow"))
        self.pushButton.setText(_translate("Home", "CLIENTI"))
        self.pushButton_2.setText(_translate("Home", "PRENOTAZIONI"))
        self.pushButton_3.setText(_translate("Home", "SERVIZI"))
        self.pushButton_4.setText(_translate("Home", "DIPENDENTI"))
        self.pushButton_5.setText(_translate("Home", "OGGETTI"))


    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_lista_oggetti_smarriti(self):
        self.vista_oggetti_persi = VistaListaOggettiPersi()
        self.vista_oggetti_persi.show()
