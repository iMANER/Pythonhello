from collections import namedtuple

'''
namedtuple:用属性而不是索引来引用tuple的某个元素

'''
#用坐标和半径表示一个圆
Circle=namedtuple('Circle',['x','y','r'])
c1=Circle(2,2,1)
print(c1.r)
print(isinstance(c1,tuple))


'''
deque:deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
支持appendleft()和popleft(),这样就可以非常高效地往头部添加或删除元素。
'''
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

'''
defaultdict:用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值
意默认值是调用函数返回的，而函数在创建defaultdict对象时传入
defaultdict的其他行为跟dict是完全一样
'''

from collections import defaultdict
dd=defaultdict(lambda :'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

'''
OrderedDict:dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
OrderedDict保持Key的顺序
'''

from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)

#Key会按照插入的顺序排列
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)

od1=OrderedDict()
od1['z']=1
od1['y']=2
od1['x']=3
print(list(od1.keys()))


#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdateOrderedDict,self).__init__()
        self._capacity=capacity

    def __setitem__(self, key, value):
        containsKey=1 if key in self else 0
        if len(self)-containsKey>=self._capacity:
            last=self.popitem(last=False)
            print('remove:',last)

        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)


A = LastUpdateOrderedDict(3)
A['one']=1
A['two']=2
A['three']=3
A['one']=11
A['four']=4
A['five']=5
print(A)

'''
ChainMap
以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
ChainMap实现参数的优先级查找
'''

from collections import ChainMap
import os,argparse

#构造缺省参数
defaults={
    'color':'red',
    'user':'guest'
}

#构造命令行参数
parser=argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace=parser.parse_args()
command_line_args={k:v for k,v in vars(namespace).items() if v }

#组合成ChainMap
combined=ChainMap(command_line_args,os.environ,defaults)

print('color=%s' %combined['color'])
print('user=%s' %combined['user'])


'''
Counter
简单的计数器，例如，统计字符出现的个数

'''

from collections import Counter
c=Counter()
for ch in '隔壁公司的程序猿 created at August 23, 2018 2:56 PM, Last updated at July 27, 2019 12:50 AM':
    c[ch]=c[ch]+1
print(c)