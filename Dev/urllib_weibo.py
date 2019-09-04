'''
POST发送一个请求，只需要把参数data以bytes形式传入
模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入

'''
from urllib import parse,request
print('Login to weibo.cn...')
user=input('User:')
passwd=input('Password:')
login_data=parse.urlencode([
    ('username',user),
    ('password',passwd),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req=request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'% (k,v))
    print('Data:',f.read().decode('utf-8'))

proxy_handler=request.ProxyHandler()

import json

def fetch_data(url):

    with request.urlopen(url) as f:

        data = f.read()

        data_str = data.decode('utf-8')

        return json.loads(data_str)

url1='http://news-at.zhihu.com/api/4/news/latest'
url2='https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest'
data = fetch_data(url1)
'''
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
'''
print(data)

print(data['stories'][1]['images'])

