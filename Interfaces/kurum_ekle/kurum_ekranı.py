#------------------------------LIBRARY--------------------#
#---------------------------------------------------------#
import sys

from PyQt5.QtWidgets import *
from Interfaces.kurum_ekle.Ui_MainWindow import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

#------------------------------CREATE DATABASE--------------------#
#--------------------------------------------------------------------#

# Use a service account
cred = credentials.Certificate(r'C:\Users\ilhan\PycharmProjects\sdgsd\setget.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
#doc_ref = db.collection('DesktopApp').document("Kurumlar")
docs = db.collection(u'DesktopApp').stream()



#------------------------------CREATE APPLICATION--------------------#
#--------------------------------------------------------------------#

App = QApplication(sys.argv)
Window=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(Window)
Window.show()


#------------------------------SAVE INFORMATIONS--------------------#
#--------------------------------------------------------------------#
def newId():
    id=random.randint(100,500)
    str_id=str(id)
    return str_id

def EKLE():
    _lneName=ui.lne_kurumismi.text()
    _spnGatewayNo=ui.spn_gatewayNo.value()
    _lneIrtibat=ui.lne_irtibatNo.text()
    _lneMail=ui.lne_iletisim_mail.text()
    _lneGatewayId=ui.lne_gatewayId.text()
    _das = ui.comboBox.currentText()
    _tbAdress=ui.textEdit.toPlainText()
    # doc_ref = db.collection(u'DesktopApp').document(u'Kurumss')

    doc_ref = db.collection('DesktopApp').document(newId())
    doc_ref.set({
        "Kurum Ismi":  _lneName,
        "Gateway Sayısı": _spnGatewayNo,
        "İrtibat Numarası": _lneIrtibat,
        "İletişim Maili":  _lneMail,
        "GatewayId": _lneGatewayId,
        "Şehir": _das,
        "Adres": _tbAdress,

    })
# ------------------------------VIEW DATA--------------------#
# --------------------------------------------------------------------#


def LISTELE():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("Id","Kurum","Gateways","Phone","Mail","Gatewat Id","City","Address"))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    row=0
    kurumName = []
    kurumDatas = []
    for doc in docs:
        # print(f'{(doc.id)} => {doc.to_dict()}')
        kurumName.append(doc.id)
        kurumDatas.append(doc.to_dict())
    print(kurumName[0])
    print(kurumDatas[0])
    ui.tableWidget.setRowCount(len(kurumDatas))
    for datas in kurumDatas:
        ui.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(newId()))
        ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(datas['Kurum Ismi']))
        ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(datas['Gateway Sayısı']))
        ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(datas['İrtibat Numarası']))
        ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(datas['İletişim Maili']))
        ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(datas['GatewayId']))
        ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(datas['Şehir']))
        ui.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(datas['Adres']))
        row=row+1




LISTELE()

# ------------------------------SINYAL SLOT--------------------
# --------------------------------------------------------------------

ui.btn_ekle.clicked.connect(EKLE)
ui.btn_listele.clicked.connect(LISTELE)


sys.exit(App.exec_())











