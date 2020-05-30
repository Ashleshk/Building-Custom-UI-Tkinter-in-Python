# import PyQT MODULE
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# DEFINE A METHOD
class Dialog(QDialog):
    NumGridRows =3
    NumButtons =4
    def __init__(self):
        super(Dialog,self).__init__()
         
        
        b1 = QPushButton("Button1")
        b2 = QPushButton("Button2")
        b3 = QPushButton("Button3")
        b4 = QPushButton("Button4")
        mainLayout =QVBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)
        mainLayout.addWidget(b3)
        mainLayout.addWidget(b4)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Box Layout")
        
if __name__ =='__main__':
    
    app=QApplication(sys.argv)
    ex=Dialog()
    sys.exit(ex.exec_())