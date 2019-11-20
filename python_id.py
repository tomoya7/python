#a = 'tomoya'
#b = 'tomoya'
a=[1,2,3]
b=[1,2,3]
#a=(1,2,3)
#b=(1,2,3)
print(id(a)==id(b))
print(a==b)

if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
a=b=[1,2,3]
print(id(a)==id(b))
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")