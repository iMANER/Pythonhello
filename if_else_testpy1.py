age=20
if age>=6: #该判断执行后就会忽略剩下的elis else
    print('teenager')
elif age>=18:
    print('adult')
else:
    print('kid')


if (3+3):#条件判断简写
    print('非零数值，非空字符串，非空list等')
if False or True:
    print('True')

brith=input('brith:')#input返回的数据类型为str，必须转换成int()类型才能比较
if int(brith)<2000: #如果输入的是字符就会报错，程序退出
    print('00前')
else:
    print('00后')
