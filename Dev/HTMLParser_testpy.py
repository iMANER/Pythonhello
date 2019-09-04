from urllib import request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag=None

    def handle_starttag(self, tag, attrs):
        if tag=='time':
            self.tag='Time:'
        elif ('class','event-location') in attrs:
            self.tag='Location:'
        elif ('class','event-title') in attrs:
            self.tag='\nTitle:'

    def handle_data(self, data):
        if self.tag:
            print(self.tag,data)

    def handle_endtag(self, tag):
        self.tag=None

with request.urlopen('https://www.python.org/events/python-events/') as f:
    html_data=f.read().decode('utf-8')

parser=MyHTMLParser()
parser.feed(html_data)