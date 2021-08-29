import sys
from PyQt5.QtWidgets import *
from homeinterface import *

App = QApplication(sys.argv)
Window=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(Window)
Window.show()

sys.exit(App.exec_())