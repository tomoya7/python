import math
a,b,c=3,4,5
if a+b>c and a+c>b and b+c>a:
	print("周长:%f"%(a+b+c))
	p=(a+b+c)/2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))  #海伦公式
	print("面积:%f"%(area))
else:
	print("不能构成三角形")