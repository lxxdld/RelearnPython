	# -*- coding: GBK -*-
def product(*L):
	summ = 1
	if len(L)==0:
		raise TypeError
	for x in L:
		summ = summ*x
	return summ 


# ����
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('����ʧ��!')
elif product(5, 6) != 30:
    print('����ʧ��!')
elif product(5, 6, 7) != 210:
    print('����ʧ��!')
elif product(5, 6, 7, 9) != 1890:
    print('����ʧ��!')
else:
    try:
        product()
        print('����ʧ��!')
    except TypeError:
        print('���Գɹ�!')

