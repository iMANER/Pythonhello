#读文件
'''
f=open('C:/Windows/PFRO.log','r')
print(f.read())
f.close()
'''

'''
try:
    f=open('C:/Windows/win.ini','r')
    print(f.read())
finally:
    if f:
        f.close()
'''

with open('C:/Windows/win.ini','r') as f:
    #print(f.read())
    for line in f.readlines():
        print(line.strip())

#二进制文件
with open('C:/Windows/1.png','rb') as f:
    print(f.read())

#字符编码
with  open('C:/Windows/win.ini','r',encoding='gbk',errors='ignore') as f:
    print(f.read())

#写文件 如果文件已存在，会直接覆盖,a追加模式
with open('C:/1.txt','a') as f:
    f.write('\nHello,World!')

print('---------------------------------')
fpath = r'C:/Windows/win.ini'

with open(fpath, 'r') as f:
    lines = f.readlines() # lines是一个列表
    for line in lines:
        print(line.strip()) # 把末尾的'\n'删掉


'''
内存读写
'''
#StringIO
from io import StringIO
f=StringIO()
f.write('Hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


s1=StringIO('hello!\nhi\ngodbye\n')
while True:
    s=s1.readline()
    if s=='':
        break
    print(s.strip())

from io import BytesIO
#BytesIO
f1=BytesIO()
f1.write('中文'.encode('utf-8'))
print(f1.getvalue())


#StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取
f2=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f2.read())


#操作文件和目录
import os

l=[]
for x in os.listdir('.'):
   if os.path.isdir(x):
       l.append(x)
print(l)

#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出当前目录下的.py文件
print([x for x in os.listdir('.')if os.path.isfile(x) and os.path.splitext('.py')])

#环境变量
print(os.environ)
print(os.environ.get('ALLUSERSPROFILE'))

#操作文件和目录
dirs=os.path.abspath('.')
print(dirs)
ndir=os.path.join(dirs,'testdir')
#os.mkdir(ndir)
#os.rmdir(ndir)


#把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('C:/Windows/1.png'))

'''
序列化
把变量从内存中变成可存储或传输的过程称之为序列化
在Python中叫pickling
'''
import pickle
d=dict(name='PANAN',age=20,score=99)
with open('1.txt','wb') as f:
    pickle.dump(d,f)
print(pickle.dumps(d))

with open('1.txt','rb') as f:
    print(pickle.load(f))

#JSON
import json
d1=json.dumps(d)
d2=json.dump(d,open('1.txt','w'))
print(d2)
print(d1)

print(json.loads(d1))

print(json.load(open('1.txt','r')))


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


#JSON进阶 class序列化和反序列化
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score



s=Student('Bob',20,99)

#首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s,default=student2dict))

#把任意class的实例变为dict
print(json.dumps(s,default=lambda obj:obj.__dict__))

#反向序列化为一个对象
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str='{"name": "Bob", "age": 20, "score": 99}'
print(json.loads(json_str,object_hook=dict2student))
print(json.loads(json_str,object_hook=lambda d:Student(d['name'],d['age'],d['score'])))


obj=dict(name='小明',age=20)
s=json.dumps(obj,ensure_ascii=True)
print(s)
