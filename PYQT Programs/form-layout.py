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
        self.createFormGroupBox()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok| QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accepted)
        buttonBox.rejected.connect(self.reject)
        mainLayout =QVBoxLayout()
        mainLayout.addWidget(self.FormGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Form Layout")
    
    
    def createFormGroupBox(self):
        self.FormGroupBox = QGroupBox("Form Layout")
        layout =QFormLayout()
        
        layout.addRow(QLabel("Name :"),QLineEdit())
        layout.addRow(QLabel("Country :"),QComboBox())
        layout.addRow(QLabel("Age :"),QSpinBox())
    
        self.FormGroupBox.setLayout(layout)
    
        
if __name__ =='__main__':
    
    app=QApplication(sys.argv)
    ex=Dialog()
    sys.exit(ex.exec_())