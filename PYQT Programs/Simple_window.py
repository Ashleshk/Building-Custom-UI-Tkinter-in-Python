# import PyQT MODULE
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QAction,QLineEdit,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# DEFINE A METHOD
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title ='PyQt5 Simple Window'
        self.left =10
        self.top  =10
        self.width = 320
        self.height =200
        self.initUI()
    
    # DEFINE METHID FOR TITLE
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.textbox=QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(280,40)
        
        
        self.button=QPushButton("Show Text",self)
        self.button.move(20,80)
        self.button.clicked.connect(self.on_click)
        
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        #print("PyQt5 Button Clicked...")
        textBoxValue= self.textbox.text()
        # POP UP MESSGAE BOX like TOAST in Andriod
        QMessageBox.question(self,'Message',"You Typed : "+textBoxValue,QMessageBox.Ok,QMessageBox.Ok)
        self.textbox.setText("");
        
        
if __name__ =='__main__':
    
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())