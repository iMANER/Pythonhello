#server.py
#从wsgiref模块导入
from wsgiref.simple_server import make_server

#导入我们自己编写的application函数
from web_hello import application

#创建一个服务器，IP 地址为空，端口8000，处理函数是application
httpd=make_server('',8000,application)
print('Serving HTTP on 8000...')

#开始监听HTTP请求
httpd.serve_forever()