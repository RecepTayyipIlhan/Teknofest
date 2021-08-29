from PyQt5.QtWidgets import *
from Interfaces.login.Ui_LoginWindow import *



App = QApplication(sys.argv)
Window=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(Window)
Window.show()

def Giris():
    kullanıcı=ui.lineEdit.text()
    password=ui.lineEdit_2.text()

    if kullanıcı=="admin" and password=="123456" :
        print("yesss beeeee")


ui.pushButton.clicked.connect(Giris)

sys.exit(App.exec_())