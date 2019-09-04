import base64
print(base64.b64encode(b'\x00 '))
print(str(b'\x00 ','utf-8'))
print(len(b'\x00'))

import struct

'''
把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写
'''
n=10240099
b1=(n&0xff000000)>>24
b2=(n&0xff0000)>>16
b3=(n&0xff00)>>8
b4=(n&0xff)
bs=bytes([b1,b2,b3,b4])
print(bs)

'''
struct模块来解决bytes和其他二进制数据类型的转换
unpack把bytes变成相应的数据类型
'''
print(struct.pack('>I',10240099))
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH',s))


bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    info=struct.unpack('<ccIIIIIIHH',data[:30])
    assert (info[0],info[1])==(b'B',b'M')
    return {
        'width':info[6],
        'height':info[7],
        'color':info[9]
    }
bi=bmp_info(bmp_data)
assert bi['width']==28
assert bi['height']==10
assert bi['color']==16
print('ok')

print(bmp_data[:30])


'''
摘要算法
'''
import hashlib

md5=hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1=hashlib.sha1()
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha256=hashlib.sha256()
sha256.update('how to use md5 in '.encode('utf-8'))
sha256.update('python hashlib?'.encode('utf-8'))
print(sha256.hexdigest())

def calc_md5(passwd):
    md5=hashlib.md5()
    md5.update(passwd.encode('utf-8'))
    return md5.hexdigest()

def login(user,passwd):
    passwd2md5=calc_md5(passwd)
    if db[user]==passwd2md5:
        return True
    else:
        return False

db={
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

import random

