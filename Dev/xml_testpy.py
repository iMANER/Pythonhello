from xml.parsers.expat import ParserCreate
from urllib.request import urlopen

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        #print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        #print(type(attrs))
        d=attrs
        for k in d:
            if k=='cityname' or k=='windState':
                print('%s:%s'%(k,attrs[k]))


    def end_element(self, name):
        pass
        #print('sax:end_element: %s' % name)

    def char_data(self, text):
        pass
        #print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

URL='http://flash.weather.com.cn/wmaps/xml/guizhou.xml'
with urlopen(URL,timeout=4) as f:
    data=f.read()

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
result=parser.Parse(data)


