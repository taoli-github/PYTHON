from datetime import datetime, timedelta


now = datetime.now()
print(now)
dt = datetime(2019,9,9,10,0)
print(dt)
print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp()))
str_time = now.strftime('%Y-%m-%d %H:%M:%S')
print(str_time)
print(datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S'))
print(now - timedelta(days=1))


from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p, p.x, p.y)


from collections import deque


q = deque([1,2,3])
q.append(4)
q.appendleft(5)
print(q)


from collections import defaultdict


dd = defaultdict(lambda :'N')
dd['1'] = 'v1'
print(dd['1'], dd[2])


from collections import OrderedDict


ordict = OrderedDict([('a',1),('c',3),('b',2)])
print(ordict)
od = OrderedDict()
od[1] = 1
od[3] = 3
od[2] = 2
print(od.keys())


class LastUpdateOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) -containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:',(key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)


lud = LastUpdateOrderDict(2)
lud[1] = 1
lud[2] = 2
print(lud)
lud[1] = 3
print(lud)


from collections import Counter


c = Counter()
for i in 'programming':
    c[i] = c[i] + 1
print(c)


import base64


print(base64.b64encode(b'ewuoewfoads'))  # base64.urlsafe_b64encode()
print(base64.b64decode('ZXd1b2V3Zm9hZHM=')) # base64.urlsafe_b64decode()


import struct
print(struct.pack('>I', 10240099))
print(struct.unpack('>I', b'\x00\x9c@c'))
# print(struct.unpack('>IH', b'\x00\x9c@c'))


import hashlib


md5 = hashlib.md5()
md5.update('hello world'.encode('utf-8'))
print(md5.hexdigest())

md5_1 = hashlib.md5()
md5_1.update('hello '.encode('utf-8'))
md5_1.update('world'.encode('utf-8'))
print(md5_1.hexdigest())


sha1 = hashlib.sha1()
sha1.update('hello world'.encode('utf-8'))
print(sha1.hexdigest())


import hmac


message = b'hello world'
key = b'secret'
hm = hmac.new(key, message, digestmod='MD5')
print(hm.hexdigest())


import itertools


natuals = itertools.count(1, 2)
# for n in natuals:
#     print(n)
nlist = itertools.takewhile(lambda x:x<=2*10-1, natuals)
print(list(nlist))
cs = itertools.cycle('ab')
# for i in cs:
#     print(i)
ns = itertools.repeat('ad', 10)
# for i in ns:
#     print(i)
for c in itertools.chain('abc', 'xy'):
    print(c)
for key, group in itertools.groupby('aaAaabbBbbeeoEoirut', lambda c: c.upper()):
    print(key, list(group))


from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s ...' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')


with create_query('bob') as q:
    q.query()


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h1'):
    print('hello world')


from contextlib import closing
from urllib.request import urlopen

#
# with closing(urlopen('http://www.python.org')) as f:
#     for l in f:
#         print(l)


from urllib import request, parse


# GET  crawl
with request.urlopen('https://www.baidu.com') as f:
    data = f.read()

    print('status:%s, %s' % (f.status, f.reason ))
    print('headers:')
    for k, v in f.getheaders():
        print('%s %s ' % (k, v))

    print('data: %s' % data.decode('utf-8'))


req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('status: %s %s ' % (f.status, f.reason))
    print('headers:')
    for k, v in f.getheaders():
        print('%s %s ' % (k, v))

    print('data: %s' % f.read().decode('utf-8'))

# Post
print('Login weibo ...')
email = input('Email:...')
password = input('Password:...')
login_data = parse.urlencode([
    ('username', email),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
reqq = request.Request('https://passport.weibo.cn/sso/login')
reqq.add_header('Origin', 'https://passport.weibo.cn')
reqq.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
reqq.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(reqq) as f:
    print('status: %s %s' % (f.status, f.reason))
    for k, v in f.getheaders():
        print(k, v)
    print('data: %s' % f.read().decode('utf-8'))


# proxy
# proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# prox_auth_handler = request.ProxyBasicAuthHandler()
# prox_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = request.build_opener(proxy_handler, prox_auth_handler)
# with opener.open('http://www.example.com') as f:
#     pass


from xml.parsers.expat import ParserCreate
from xml.etree.ElementTree import parse


class DefaultSaxHandler(object):
    def start_element(self, name, attr):
        print('sax:start_ele %s attr %s' % (name, str(attr)))

    def end_element(self, name):
        print('sax:end_ele %s ' % name)

    def char_data(self, text):
        print('sax:char_data %s' % text)


xml_str = '''<?xml version='1.0'?>
<language type='common'>
<kind country='china'>Chinese</kind>
<kind country='japan'>English</kind>
</language>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml_str)


from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHtmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('start_tag:<%s> attr:' % (tag, str(attrs)))

    def handle_endtag(self, tag):
        print('end_tag:</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('start_end_tag:<%s/> attr:' % (tag, str(attrs)))

    def handle_data(self, data):
        print('data:%s' % data)

    def handle_comment(self, data):
        print('<!- comment:%s ->' % data)

    def handle_entityref(self, name):
        print('&%s' % name)

    def handle_charref(self, name):
        print('&#%s' % name)


# with urlopen('https://www.python.org/events/python-events/') as f:
#     html = f.read()
#     parser.feed(str(html))

parser = MyHtmlParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')