# -*- coding: GBK -*-
#�붨��һ������quadratic(a, b, c)������3������������һԪ���η��� ax^2+bx+c=0ax 
#2+bx+c=0 �������⡣
import math
def quadratic(a,b,c):
	if (b*b-4*a*c)<0:
		print("no resule")
		return 0
	else:	
		x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
		return x1,x2
meiling={"mei":"xing","ling":"ling"}
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('����ʧ��')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('����ʧ��')
else:
    print('���Գɹ�')
print(meiling["mei"])
