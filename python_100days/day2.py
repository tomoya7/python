import math
def temprature(f):
	c=(f-32)/1.8
	print('%.1f华氏度=%.1f摄氏度'%(f,c))
def cicle(r):
	perimeter=2*math.pi*r
	area=math.pi*r**2
	print('周长:%.2f,面积:%.2f'%(perimeter,area))
def leap(year):
	is_leap=(year % 400== 0 or year % 4 == 0 and year % 100 !=0)
	print(is_leap)
if __name__=="__main__":
	temprature(100)
	cicle(3)
	leap(2004)
	print(chr(65))
	print(ord('A'))


