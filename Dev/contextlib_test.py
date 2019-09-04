'''
不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句
实现上下文管理是通过__enter__和__exit__这两个方法实现的
'''

class Query(object):
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...'% self.name)


with Query('Bob') as q:
    q.query()



'''
@contextmanager
Python的标准库contextlib提供了更简单的写法
'''

from contextlib import contextmanager

class Query1(object):
    def __init__(self,name):
        self.name=name

    def query(self):
        print('Query info about %s...'% self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q=Query1(name)
    yield q
    print('End')

with create_query('An') as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>"% name)
    yield
    print("<%s>"% name)

with tag('h1'):
    print('hello')
    print('world')


'''
可以用closing()来把该对象变为上下文对象
'''

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)