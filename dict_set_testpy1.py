d={'PAN':10,'AN':20,'PANAN':30}#key-value存储方式，速度快
print(d['AN'])

d['ANAN']=40 #除了初始化指定的外，还可以通过key 放入
print(d)

d['ANAN']=50 #key只能对应一个value,所以多次放入同一个key，后面的值会把前面的值替换掉
print(d)

'''
如果key 不存在，dict会报错，避免key不存在的错误有两种方法
1、通过in判断key 是否存在
2、通过get方法，如果key不存在，返回none或者指定的值
注：通过key 计算位置的算法成为hash 算法
'''
print('ANAN' in d)
print(d.get('a','dict中a不存在'))

print(d.pop('AN'))#删除key

'''
set
与dict类似也是一组key的集合，在set中key不能重复，且不存储value
创建一个set需要提供一个list作为输入集合
'''
s=set([1,2,2,3])
print(s)#重复元素自动过滤
s.add(5)
print(s)#add()方法可以添加元素到set中，可以重复添加，但会自动过滤
s.remove(3)
print(s)#删除元素

s1=set([1,2,3])
s2=set([2,3,4,5])
print(s1 & s2) #数学交集运算
print(s1 | s2) #数学并集运算
print(s2 - s1) #数学差集运算
print(s1 - s2) #数学差集运算

'''
不可变对象与可变对象
str 与 list
'''
a=['e','b','c']
a.sort()
print(a)

a1='ecb'
print(a1.replace('e','E'))#replace方法创建了一个新的字符串并返回
print(a1) #仍然指向原来的字符串