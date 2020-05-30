# import PyQT MODULE
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# DEFINE A METHOD
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title ='PyQt5 horizontal Layout'
        self.left =10
        self.top  =10
        self.width = 320
        self.height =100
        self.initUI()
    
    # DEFINE METHID FOR TITLE
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.createHorizontalLayout()
        windowlayout=QVBoxLayout()
        windowlayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowlayout)
        self.show()
    
    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("Fav Color")
        layout =QHBoxLayout()
        
        buttonBlue=QPushButton('Blue',self)
        buttonBlue.clicked.connect(self.on_click)
        layout.addWidget(buttonBlue)
        
        buttonRed=QPushButton('Red',self)
        buttonRed.clicked.connect(self.on_click)
        layout.addWidget(buttonRed)
        
        buttonGreen=QPushButton('Green',self)
        buttonGreen.clicked.connect(self.on_click)
        layout.addWidget(buttonGreen)
        
        self.horizontalGroupBox.setLayout(layout)
    
    @pyqtSlot()
    def on_click(self):
        print("pyqt5 button click")
        
if __name__ =='__main__':
    
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())