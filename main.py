import sys

from PyQt5.QtWidgets import QApplication

import home.views.vistahome

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = home.views.vistahome.VistaHome()
    vista_home.show()
    sys.exit(app.exec())


