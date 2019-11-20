#打印杨辉三角
def yh():
    num = int(5)
    yh=[[]] *num
    for row in range(len(yh)):
    	yh[row]=[None] *(row+1)
    	for col in range(len(yh[row])):
    		if row==0 or row==col:
    			yh[row][col]=1
    		else:
    			yh[row][col]=yh[row - 1][col] + yh[row - 1][col - 1]
    		print(yh[row][col],end='\t')
    	print('',end='\n')
#约瑟夫环问题
def ysf():
	persons=[True]*30
	counter,index,number=0,0,0
	while counter<15:
		if persons[index]==True:
			number+=1
			if number==9:
				persons[index]=False
				counter+=1
				number=0
		index+=1
		index%=30
	for person in persons:
		print('基' if person else '非',end='')	
if __name__=="__main__":
	yh()
	ysf()