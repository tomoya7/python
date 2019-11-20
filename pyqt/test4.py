import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget
 
 
class Communicate(QWidget):
    
    closeApp = pyqtSignal(str) 
    
 
class Example(QMainWindow):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        self.c = Communicate()
        self.c.closeApp.connect(self.close1)       
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
    
    def close1(self,str1):
        print('str1')    
        self.close()
        
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit('tomoya')
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
