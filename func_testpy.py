'''
递归函数
函数调用是通过栈(stack)这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当
函数返回，栈就会减一层栈帧，栈的大小是有限的，所以递归调用的次数过多会导致栈溢出
'''
def fact(n): #递归函数计算n 阶乘
    if n==1:
        return 1
    return n*fact(n-1) #乘法表达式

'''
尾递归：解决递归调用栈溢出的方法是通过尾递归优化，与循环效果一样
函数返回时调用函数自身，且return语句不含表达式
'''
def fac1(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return  product
    return fact_iter(num-1,num*product)


'''
切片：首位空格
递归方法
'''
def testtrim(s):
    if  ' ' not in s[0]+s[-1]:
        pass

def trim(s):
    if s == '' or ' ' not in s[0]+s[-1]:
        return s
    if s[0] == ' ':
        return trim(s[1:])
    return trim(s[:-1])

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


'''
迭代：
查找一个list中最小和最大值，并返回一个tuple
'''
def findMinAndMax(numbers):
    if not numbers:
        return (None,None)
    min,max=numbers[0],numbers[0]
    for i in numbers:
        min=i if i<min else min
        max=i if i>max else max
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


print(list(range(1)))

#杨辉三角
def triangles():
    L=[1]
    yield L
    while True:
        L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)] +[1]
        yield L #遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

n=0
results=[]
for  t in triangles():
    print(t)
    results.append(t)
    n=n+1
    if n==10:
        break


print(list(range(1)))

