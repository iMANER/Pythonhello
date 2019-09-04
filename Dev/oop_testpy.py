'''
1、数据封装
2、给类增加新的方法
3、访问限制
'''

class Student(object):

    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s:%s'% self.__name,self.__score)

    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

    #访问限制测试
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')

#测试
bart=Student('Bart Simpson',59)
#print(bart.score)

lisa=Student('Lisa',99)
#print(lisa.name,lisa.get_grade())
#print(bart.name,bart.get_grade())


if lisa.get_name()!='Lisa':
    print('测试失败！')
else:
    lisa.set_name('Bart')
    if lisa.get_name()!='Bart':
        print('测试失败!')
    else:
        print('测试成功!')