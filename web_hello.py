def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body='<h1>Hello,%s!</h1>'% (environ['USERNAME'][0:] or 'Web')
    return [body.encode('utf-8')]