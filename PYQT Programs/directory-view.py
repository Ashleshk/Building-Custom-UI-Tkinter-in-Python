# import PyQT MODULE
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# DEFINE A METHOD
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title ='PyQt5 file system view'
        self.left =10
        self.top  =10
        self.width = 640
        self.height =400
        self.initUI()
    
    # DEFINE METHID FOR TITLE
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.model =QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.show()
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        
        self.tree.setWindowTitle("DirView")
        self.tree.resize(640,480)
        
        WindowLayout =QVBoxLayout()
        WindowLayout.addWidget(self.tree)
        self.setLayout(WindowLayout)
        self.show()
   
        
if __name__ =='__main__':
    
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())