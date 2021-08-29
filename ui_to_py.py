from PyQt5 import uic

with open('Interfaces/home_interface/homeinterface.py', "w" , encoding="utf-8") as fout:
    uic.compileUi('Interfaces/home_interface/homeinterface.ui', fout)
