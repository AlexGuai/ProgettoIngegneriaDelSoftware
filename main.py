from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from home.views.VistaHome import Ui_Home
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Home()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())