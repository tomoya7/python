class Test(object):
	def __getMessage(self):
		print('tomoya')
	def _getMessage(self):
		print('ingen')
if __name__=="__main__":
	test=Test()
	#test.__getMessage()
	test._Test__getMessage()
	test._getMessage()
