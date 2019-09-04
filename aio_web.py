import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text='<h1>Hello,%s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init():
    app=web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    runner=web.AppRunner(app)
    await runner.setup()
    #app.router.add_route('GET','/',index)
    #app.router.add_route('GET','/hello/{name}',hello)
    #srv=await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    srv=web.TCPSite(runner,'127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    await srv.start()


loop=asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()