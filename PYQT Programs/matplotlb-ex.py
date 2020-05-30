from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random
# DEFINE A METHOD
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title ='PyQt5 matplotlib example'
        self.left =10
        self.top  =10
        self.width = 640
        self.height =400
        self.initUI()
    
    # DEFINE METHID FOR TITLE
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        m =PlotCanvas(self,width=5,height=4)
        m.move(0,0)
        button = QPushButton('PyQt5 Button',self)
        button.setToolTip('This is an example Button')
        button.move(500,0)
        button.resize(140,100)
        self.show()
    
class PlotCanvas(FigureCanvas):
    def __init__(self,parent=None,width=5,height=4,dpi=100):
        fig =Figure(figsize=(width,height),dpi=dpi)
        self.axes =fig.add_subplot(111)
        
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
        
        
    def plot(self):
        data = [random.random() for i in range(25)]
        ax =self.figure.add_subplot(111)
        ax.plot(data,'r-')
        ax.set_title('PyQT matplotlib examle')
        self.draw()
        
    
        
if __name__ =='__main__':
    
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())