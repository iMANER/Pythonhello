

'''
_slots
'''

class Student(object):
    __slots__ = ('name','set_age','score','age')

#实例绑定属性
s=Student()
s.name='ANPAN'
print(s.name)

#实例绑定方法
def set_age(self,age):
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

#给所有实例绑定方法，可以给class 绑定方法
def set_score(self,score):
    self.score=score

Student.set_score=set_score #绑定方法
s1=Student()
s2=Student()

s1.set_score(100)
print(s1.score)

s2.set_score(99)
print(s2.score)

'''
定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
仅对当前类实例起作用，对继承的子类是不起作用
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''

class GraduateStudent(Student):
    __slots__ = ('math1')

g=GraduateStudent()
g.math=100
print(g.math)