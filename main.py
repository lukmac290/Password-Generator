#Author: Łukasz Maciejewski
#https://github.com/lukmac290
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import random

smallLetters = "sdfrtghqpazxyuiwjklcvbenmo"
capitalLetters = "POIUYTREWQZXCVBNMASDFGLKJH"
numbers = "2537168490"
specialCharacters = "^,<.{&_:?=+`~!(%\|[@)-#$>*}];/"

class Generator(QMainWindow):

    def __init__(self):
        super(Generator,self).__init__()
        loadUi("pwGenGUI.ui",self)
        self.generateButton.clicked.connect(self.generatePassword)
        self.copyButton.clicked.connect(self.copyToClipboard)
    
    def generatePassword(self):
        password = ""
        charPool = ""

        if self.smallLettersChbx.isChecked():
            charPool += smallLetters
        if self.capitalLettersChbx.isChecked():
            charPool += capitalLetters
        if self.numbersChbx.isChecked():
            charPool += numbers
        if self.specialCharactersChbx.isChecked():
            charPool += specialCharacters

        for i in range(self.pwLength.value()):
            password += random.choice(charPool)
        
        self.lineEdit.setText(password)

    def copyToClipboard(self):
        clipB = QApplication.clipboard()
        clipB.clear(mode=clipB.Clipboard)
        clipB.setText(self.lineEdit.text(), mode=clipB.Clipboard)

app = QApplication(sys.argv)
mainWindow = Generator()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedSize(380,200)
widget.setWindowTitle("Password Generator")
widget.setWindowIcon(QtGui.QIcon('padlock.jpg'))

widget.show()
app.exit(app.exec_())