names=['PAN','AN','PANAN']
print(names)
for name in names: #依次把list或者tuple中的每个元素迭代出来
    print(name)

sum1=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum1=sum1+x
print(sum1)

#range()函数生成整数序列
print(list(range(5)))

sum=0
for x in range(101):
    sum=sum+x #print缩进在循环内，不缩进在循环外
print(sum)

sum2=0
n=100
while n>0: #while循环，只要条件满足就不断循环，条件满足时退出
    sum2=sum2+n
    n=n-1
print(sum2)
print(n)


