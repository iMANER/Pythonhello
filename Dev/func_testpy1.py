def f(x):
    return x*x

#用map函数可以实现作用在一个list上
r=map(f,[1,2,3,4,5,6])
#r是一个Iterator惰性序列，需要用一个list 把整个序列计算出来并返回一个list
print(list(r))

#把list转换成字符串
print(list(map(str,[1,2,3,4,5,6])))

'''
reduce
reduce把一个函数作用在一个序列上，这个函数必须接受两个参数，reduece把结果与这个序列的下一个
元素做累计计算
'''
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5]))

def fn(x,y):
    return x*10+y
#str转换为int
def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
print(reduce(fn,map(char2num,'13579')))

print(list(map(char2num,'13579')))


def sum(x, y):
    return x + y

'''
lambda函数用法
匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
'''
p = lambda x,y:x+y
print(p(4,6))

print(reduce(lambda x,y:x*10+y,map(char2num,'13579')))

#人名规范化
def normalize(name):
    L=[]
    L=name[0].upper()+name[1:].lower()
    return L
print(list(map(normalize,['adam', 'LISA', 'barT'])))

#求积
def prod(L):
    return reduce(lambda x,y:x*y,L)
print(prod([3, 5, 7, 9]))

print('123.456'.index('.'))#查找.所在字符串的下标

#字符串转浮点数
def str2float(s):
    i=s.index('.')
    s1=s[:i]+s[i+1:]
    print(isinstance(s1,str))
    print(len(s[i+1:]))
    return reduce(lambda x,y:x*10+y,map(char2num,s[:i]+s[i+1:]))/10**len(s[i+1:])
print(str2float('123.456'))

#测试负指数幂确定小数点位置
print(1234567/10**3)

'''
sorted高阶函数
'''
def by_name(a):
    return a[0]


L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L1,key=by_name))

print(L1[0][0],L1[0][1])

'''
返回函数
'''
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()

'''
结果一样的原因是在于返回的函数引用了变量i，但它并非立即执行
等到三个函数都返回时，它们所引用的变量i都变成了3
'''
print(f1(),f2(),f3())

'''
如何引用环境变量？
方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
'''
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for x in range(1,4):
        fs.append(f(x))
    return fs

t1,t2,t3=count1()
print(t1(),t2(),t3())

'''
匿名函数
'''
#赋值给变量
f=lambda x:x*x
print(f(5))

#匿名函数作为返回值返回
def build(x,y):
    return lambda :x*x+y*y

f1=build(2,3)
print(f1())


print(list(filter(lambda n:n%2==1,range(1,20))))
print(f1.__name__)

'''
装饰器：在代码运行期间动态增加功能的方式
'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2019-07-16')

#print(now())
now=log(now)
print(now())

#decorator本身需要传入参数
def log1(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'% (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log1('execute')
def now1():
    print('2019-07-16')

print(now1.__name__)

print(now1())

'''
Python内置的functools.wraps
把原始函数的__name__等属性复制到wrapper()函数中
'''
import functools
def log2(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper

@log2
def now2():
    print('2019-07-16')

print(now2.__name__)
print(now2())

#针对带参数的decorator
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():'% (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log3('execute')
def now3():
    print('2019-07-16')

print(now3.__name__)
print(now3())

