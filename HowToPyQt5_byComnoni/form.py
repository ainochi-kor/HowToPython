import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#ui파일을 가져옴
UIFile = "UI\dialog.ui"


app = QApplication(sys.argv)
mainDialog = QDialog()
uic.loadUi(UIFile, mainDialog)
mainDialog.show()
app.exec_()