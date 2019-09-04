import time
import functools
import tensorflow as tf


start=time.time()
for x in range(1,100000):
    x%2==1
end=time.time()
print(end-start)

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start=time.time()
        f=fn(*args,**kw)
        end=time.time()
        print('%s executed in %s ms'% (fn.__name__,end-start))
        return f
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y
@metric
def slow(x,y,z):
    time.sleep(1.1234)
    return x*y*z

f=fast(11,22)
s=slow(11,22,33)
if f!=33:
    print('测试失败！')
elif s!=7986:
    print('测试失败！')

#针对带参数的decorator
def metric1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            start=time.time()
            f=func(*args,**kw)
            end=time.time()
            print('%s %s in %s ms')% (func.__name__,end-start)
            return f
        return wrapper
    return decorator

'''
decorator同时可以处理代参和不代数
'''
def log(func):
    if isinstance(func,str):
        text=func
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('%s %s():'% (text,func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s():' %  func.__name__)
        f=func(*args, **kw)
        print('end call %s():' %  func.__name__)
        return f
    return wrapper

@log
def f():
    print(time.gmtime().tm_sec)

@log('executed')
def f1():
    print(time.gmtime().tm_sec)

print(f())
print(f1())
print(time.gmtime()[0])


'''
偏函数测试
'''
max2=functools.partial(max,1)
print(max2(5,6,7))

