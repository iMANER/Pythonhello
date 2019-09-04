import hmac,random

message=b'Hello,world!'
key=b'secret'
h=hmac.new(key,message,digestmod='MD5')
print(h)
print(h.hexdigest())

def hamc_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),digestmod='MD5').hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username=username
        self.key=''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password=hamc_md5(self.key,password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user=db[username]
    return user.password==hamc_md5(user.key,password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


'''
模块itertools提供了非常有用的用于操作迭代对象的函数
'''

import itertools
def pi(n):
    natuals=itertools.count(1,2)
    ns=itertools.takewhile(lambda x:x<=2*n-1,natuals)
    return sum([4/x if x%4==1 else -4/x for x in list(ns)])


print(1%4)
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

