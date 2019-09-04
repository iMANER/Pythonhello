'''
素数：
方法是埃氏筛法
使用filter高阶函数
'''
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()#初始化序列
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible,it)

for n in primes():
    if n <10:
        print(n)
    else:
        break

'''
回数
使用filter高阶函数
'''
def is_palindrome(n):
    return n==int(str(n)[::-1])

print(list(filter(is_palindrome,range(100,120))))
print(int(str(123)[::-1]))