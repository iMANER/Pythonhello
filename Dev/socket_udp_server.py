import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9998))
print('Bind UDP on 9998')
while True:
    data,addr=s.recvfrom(1024)
    print(bytes.decode(data))
    print('Received from %s:%s.'% addr)
    print(type(addr))
    #print('Received %s from %s:%s'%(bytes.decode(data)+addr))
    s.sendto(b'Hello,%s'% data,addr)

