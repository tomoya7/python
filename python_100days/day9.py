#property装饰器
class Person(object):
	__slots__=('_age','_name')
	def __init__(self,age):
		super().__init__()
		self._age=age
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self,age):
		if age<18:
			raise 'biger'
		self._age=age
if __name__=='__main__':
	person=Person(18)
	#person.age=17
	person.age=19
	print(person._age)
	person._name='tomoya'
	print(person._name)
	#person._gender='men'
	print([(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)])


