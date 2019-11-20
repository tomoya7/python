from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication
import sys
class MyThread(QThread):
	def __init__(self):
		super(MyThread,self).__init__()
	def run(self):
		print('tomoya')
if __name__=="__main__":
	app=QApplication(sys.argv)
	t1=MyThread()
	t1.start()
	sys.exit(app.exec_())