from abstest import  my_abs,move,quadratic,power,power1,enroll,add_end,calc,person,person1
import math
#测试my_abs
print(my_abs(-20))
print(my_abs(99))
#print(my_abs('a'))

#测试move
x,y=move(100,100,60,math.pi/6)#返回的是一个tuple，可以使用多个变量接收，按位置赋值给变量
print(x,y)

z=move(50,50,30,math.pi/6)#返回tuple,在语法上返回一个tuple可以省略括号
print(z)

#测试二元一次方程式跟求解
print(math.sqrt(2))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print('quadratic(1, 3, -4) =', quadratic(4, 1, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 2, 1))

if quadratic(2,3,1)!=(-0.5,-1.0):
    print('测试失败')
if quadratic(1,3,-4)!=(1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')
#print('quadratic(b, 2, 1) =', quadratic(1, 'c', 1))

'''
函数的参数测试
'''
print(power(4))
print(power1(2,11))
print(enroll('Sara','F'))
print(enroll('Andi','M',city='天津'))
print(add_end(['1','2','3']))
print(add_end(['4','5']))
print(add_end())
#测试可变参数
nums=[1,2,3]
print(calc(*nums))
print(calc())

#关键字参数测试
print(person('ANAN',20))
print(person('ANAN',20,city='beijing'))
print(person('ANAN',20,city='beijing',job='Engineer'))
extra={'city':'beijing','job':'engineer'}
print(person('ANAN',20,**extra))

print(person1('ANAN',20,**extra))
