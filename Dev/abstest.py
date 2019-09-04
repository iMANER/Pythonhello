import math
'''
返回多个值
例如游戏计算一个点移动到另一个点，给出坐标、位移、角度计算新坐标
'''
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny

'''
计算二元一次方程式的根
根公式求解
'''
def quadratic(a,b,c):
    if not isinstance(a,(float,int)) :
        raise TypeError('bad operand type')
    if not isinstance(b,(float,int)) :
        raise TypeError('bad operand type')
    if not isinstance(c,(float,int)) :
        raise TypeError('bad operand type')

    m1 = math.pow(b, 2) - 4 * a * c#判别式
    if a==0:
        return 'a不能等于0'
    if m1>=0:
        x1=(-b+math.sqrt(m1))/(2*a)
        x2=(-b-math.sqrt(m1))/(2*a)
        return x1,x2
    else:
        return '解是一对共轭复根'

def my_abs1(x):
    pass #空函数占位，缺少pass就会出现语法错误

def my_abs(x):
    if not isinstance(x,(int,float)):#isinstance对参数类型做检查，只允许int float类型的参数
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

    '''
   函数的参数的顺序
    1、必选参数
    2、默认参数
    3、可变参数
    4、命名关键字参数
    5、关键字参数
    6、这5种参数都可以组合使用
    7、特殊的tuple和dict，可以调用上述函数，类似func(*args,**kw)
    '''

#计算x的平方
def power(x):
    return x*x

#计算n次方
def power1(x,n):
    sum1=1
    while n>1:
        n=n-1
        sum1=sum1*x
    return sum1

#默认参数
def enroll(name,gender,age='0',city='北京'):
    print('Name ',name)
    print('Gender',gender)
    print('Age',age)
    print('City',city)
#list默认参数测试
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

#可变参数测试
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum


#关键字参数测试
def person(name,age,**kw):
    if 'city' in kw: #检查传入的参数
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

#命名关键字参数测试
def person1(name,age,*,city,job):
    print(name,age,city,job)