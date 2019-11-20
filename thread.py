from threading import Thread
import threading
class MyThread(Thread):
	"""docstring for MyThread"""
	def __init__(self):
		super(MyThread, self).__init__()
		self.__running=threading.Event()
		self.__running.set()
		#self.__running.clear()
	def run(self):
		if self.__running.isSet():
			print("tomoya")
if __name__=='__main__':
	t1=MyThread()
	t1.start()