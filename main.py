#Author: Łukasz Maciejewski
#https://github.com/lukmac290
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from generator import Generator

app = QApplication(sys.argv)
mainWindow = Generator()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedSize(380,200)
widget.setWindowTitle("Password Generator")
widget.setWindowIcon(QtGui.QIcon('padlock.jpg'))

widget.show()
app.exit(app.exec_())