# -*- coding: GBK -*-
resource=['a','a','b','a','b','c']
resource1=['a','a','b','a','b','c','D','D']
#dict�ֵ����ÿռ任ȡʱ��
#����get(),���key�����ڣ����Է���None�������Լ�ָ����value��
dic={}
dic1={}
for element in resource:
	result=dic.get(element,-1)
	if result==-1:#dic�в�����element
		dic[element]=1#����dic�У�valΪ1
	else :
		dic[element]+=1
print(dic)
i=0		
for element in resource1:
	result=dic1.get(element)
	if not result:#û���ֹ�
		dic1[element]=1
	else :#���ֹ�
		dic1[element]+=1
print(dic1)		
		
