# -*- coding: GBK -*-
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count +=1


        
# test:
if Student.count != 0:
    print('����ʧ��!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('����ʧ��!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('����ʧ��!')
        else:
            print('Students:', Student.count)
            print('����ͨ��!')

