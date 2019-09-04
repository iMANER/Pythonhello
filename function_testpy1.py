'''
abs()
交互式命令行通过help(abs)查看abs 帮助信息
只能传入一个正确的参数类型，比如str会报TypeError错误
'''
print(abs(-100))
print(abs(100))
print(abs(12.34))

a1=abs#把函数赋给一个变量等于把变量a 指向abs
print(a1(-99))#通过a调用abs函数

#max函数可以接受任意多个正确的参数类型并且返回最大的哪个
print(max(1,2,3,4))
print(max(-4,-5,-1))

#数据类型转换
print(int('123'))
print(int(12.34))
print(float(12.34))
print(str(123))
print(bool(1))
print(bool(0))
print(bool(''))

