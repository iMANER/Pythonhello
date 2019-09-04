from  func_testpy import fact,fac1
from collections.abc import Iterable

#import builtins; builtins.abs = 10

#测试fact阶乘计算函数 递归调用
print(fact(4))

print(fac1(9))


'''
汉诺塔
'''
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,'A','B','C')

#测试是否可迭代
print(isinstance('ABC',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
print(isinstance('123',Iterable))

#enumerate可以把一个list变成索引-元素对
for i,value in enumerate([1,2,3]):
    print(i,value)


#列表生成式
print(list(range(1,11)))

L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

print([x*x for x in range(1,11)])

print([x*x for x in range(1,11) if x%2==0] )

print([m+n for m in 'ABC' for n in 'XYZ'])

L1=['Hello', 'World', 'IBM', 'Apple']
print([ s.lower() for s in L1])

L2 = ['Hello', 'World', 18, 'Apple', None]


L2=[x.lower() for x in L2 if isinstance(x,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


'''
生成器：
斐波那契数列
'''
L3=(x*x for x in range(10))
print(L3)
print('next：',next(L3))#交互式环境下测试

#循环
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

fib(6)

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print('yield 测试')
for x in fib1(10):
    print(x)

#拿return返回值
g=fib1(4)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

print(abs)
