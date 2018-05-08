# _*_ coding:utf-8 _*_
import time
from collections import Iterable
from collections import Iterator
import functools
from functools import reduce
import os
import types
import Hello
import OOP
from enum import Enum, unique
import logging
import os


print(ord('A'))

print('xiaoli salary is %d, work in %s.' % (1000000, 'Apple Inc'))

print(r'\\')
print('''this is 
a novel written
by Mark!
''')

print('拉的说法'.encode('UTF-8'))
# list
classmates = ['zhangssan', 'lisi']
print(classmates[0])
print(classmates)
classmates.append('wangwu')
print(classmates)
classmates.insert(1, 'zhaosi')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
# tuple
t = (1,)
print(t)
t = (1,2)
print(t)
print(t[0])

age = 6
if age > 1:
    print(age)
else:
    print('dsfa')

print(list(range(5)))

multi = lambda x, y: x*y

res = multi(3, 5)
print(res)
# dict
dic = {"limuxi": 100,"guoliyan": 99}

print(dic, dic['limuxi'])
print(dic.get('guoliyan'))
for key in dic:
    print(key)
    print(dic[key])
dic.pop('limuxi')
print(dic)

li = [3, 1, 2]
print(li)
se = set(li)
print('se',se)

se.add(4)
print(se)

se.remove(4)
print(se)

li.sort()
print(li)

lii = li[:]
print(lii)

a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)


def nop():
    pass


def return_val(x, y):
    return x, y


val = return_val(1.0, 2.0)
print(val)
x, y = return_val(1.0, 2.0)
print(x, y)


def add_end(l=[]):
    l.append("end")
    print(l)


add_end()
add_end()
add_end()


def calc_num(*numbers):
    sum = 0;
    for x in numbers:
        sum = sum + x * x
    print(sum)


calc_num(1, 2, 3)
calc_num(*li)


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('likeqiang', 89, position='beijing', rank='ceo')
extra = {"city":'beijing', 'job':'engineer'}
person('xijinping', 30, **extra)


def person(name, age, *, job):
    print('name:', name, 'age:', age, 'other:', job)


person('litao', 30, job='hel')
print(isinstance(extra, Iterable))

l = ['a', 'b', 'c']
for i, v in enumerate(l):
    print(i, v)


# jiecheng feibonaqieshulie hannuota:recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


s_time = time.time()
print(factorial(5))
e_time = time.time()
print(e_time - s_time)


def tail_factorial(n, temp):
    if n == 1:
        return temp
    return tail_factorial(n-1, n*temp)


s_time = time.time()
print(tail_factorial(10, 1))
e_time = time.time()
print(e_time - s_time)


def fabonacci(n):
    if n <= 2:
        return 1
    return fabonacci(n-1) + fabonacci(n-2)


s1 = time.time()
print(fabonacci(5))
e1 = time.time()
print(e1-s1)


def tail_fabonacci(n, last, result):
    if n == 0:
        return last
    return tail_fabonacci(n-1, result, result + last)


print(tail_fabonacci(5, 0, 1))


print(list(range(1,11)))
print(list(range(11)))
l_q = [x*x for x in range(1,11)]
print(l_q)
l_e_q = [x*x for x in range(1, 11) if x % 2 == 0]
print(l_e_q)
l_m = [m+n for m in 'AB' for n in 'XYZ']
print(l_m)



def hanoi(n, a, b, c):
    if n == 1:
        print(a + '->' + c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')


dir_con = [d for d in os.listdir('..')]
print(dir_con)

dd = {'x': 'A', 'y': 'B', 'z': 'C'}
dd_res = [k + '=' + v for k, v in dd.items()]
print(dd_res)

dd_lower = [s.lower() for s in dd.values()]
print(dd_lower)

L1 = ['HELLO', 'WORLD', 18, 'IM LITAO']
L1_LOWER = [s.lower() for s in L1 if isinstance(s, str)]
print(L1_LOWER)

#generator
l = [x*x for x in range(11)]
print(l)
l_g = (x*x for x in range(11))
print(l_g)
print(next(l_g), next(l_g))

for g in l_g:
    print(g)

def fib(num):
    n, k, j = 0, 0, 1
    while n < num:
        # print(j)
        yield j
        k, j = j, (k+j)
        n = n + 1
    return 'ok'


f = fib(8)
for ff in f:
    print(ff)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
for oo in o:
    print(oo)


print('------')
for ii in range(2):
    print(ii)


# yanghui triangle
def yanghui_tri(num):
    a = [1]
    while len(a) <= num:
        print(a)
        # yield(a)
        a = [sum(i) for i in zip([0] + a, a + [0])]


yanghui_tri(5)


def yanghui_tri_1(num):
    b = [1]
    while len(b) <= num:
        # print(b)
        # b = [0] + b + [0]
        yield b
        b.insert(0, 0)
        b.append(0)
        b = [b[i]+b[i+1] for i in range(len(b)-1)]


g_b = yanghui_tri_1(5)
print(g_b)
for gb in g_b:
    print(gb)

print(isinstance(g_b, Iterable))
print(isinstance(g_b, Iterator))


# Iterator
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))

it = iter(classmates)
while True:
    try:
        print(next(it))
    except StopIteration as e:
        print('StopIteration Error:Iterator has no items!')
        break


# high-order function
def add(x, y, f):
    return f(x) + f(y)


print(add(-1, 5, abs))


# map
def f(x):
    return x*x


result = map(f, [1, 2, 3])
print(list(result))
for r in result:
    print(r)

print(list(map(str, [1, 2, 3, 4, 5])))


# reduce
def add(x, y):
    return x + y


print(reduce(add, [1,2,3,4,5]))
print(sum([1,2,3,4,5]))


def trans(x, y):
    return x*10 + y


print(reduce(trans, [1,2,3,4,5]))


def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]


print(list(map(char2num, '12345')))
print(reduce(trans, map(char2num, '12345')))
print(reduce(lambda x,y:x*10+y, map(char2num, '12345')))

title_list = ['adam', 'ASFDF', 'DSFdfAfdfde']


def normalize(name):
    return name.title()


print(list(map(normalize, title_list)))


def prod(listt):
    def prodcutt(x, y):
        return x*y
    print(reduce(prodcutt, listt))


prod([3, 5, 7, 9])


# filter
def is_odd(x):
    return x%2 == 1


print(list(filter(is_odd,[1,2,3,4,5])))


def is_empty(s):
    return s and s.strip()


print(list(filter(is_empty, ['a','','b',None,'c'])))


def odd_series():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisble(n):
    return lambda x : x % n > 0


def primes():
    yield 2
    it = odd_series()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisble(n), it)


prime = primes()

for p in prime:
    if p < 100:
        print(p)
    else:
        break


l = [1,2,3,4,5]
print(l[-1], l[::-1])


def rer_num(n):
    return str(n) == str(n)[::-1]


print(list(filter(rer_num, list(range(20000)))))


# sorted
print(sorted([2,5,2,-4,7,-9,1], key=abs, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def sort_rule(t):
    return t[1]


print(sorted(L, key=sort_rule, reverse=True))


# Closure
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            n += 1
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1,2,3,4,5)
print(f)
print(f())


def count():
    fs = []
    for i in range(1, 3):
        def f():
            print(i)
            return i*i
        fs.append(f)
    return fs


f1, f2 = count()
print(f1(), f2())


def count_1():
    fs = []
    def f(i):
        def g():
            return i*i
        return g
    for k in range(1, 3):
        fs.append(f(k))
    return fs


f1, f2 = count_1()
print(f1(), f2())


def create_counter():
    s = 0

    def addd():
        nonlocal s
        s += 1
        return s
    return addd


c1 = create_counter()
print(c1())

# lambda
print(list(filter(lambda x: x % 2 == 1, range(1, 21))))

print('&&&&&&&&&&&&&&&+=========================&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+++++++++==========')
# decorator
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('call %s()' % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print(time.time())


f = now
f()
print(f.__name__)


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('&&&&&&&')
        print(args)
        print(args[0].sheet)
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kw)
    return wrapper

class TestDec:
    def __init__(self):
        self.sheet = ''

    @metric
    def fast(self,x, y):
        time.sleep(0.0012)
        return x+y


f = TestDec().fast(11, 22)
# if f != 33:
#     print('failure')
# else:
#     print('success')
f = TestDec()
f.sheet = ''
ress = f.fast(11, 22)
print(ress)

def log_1(obj=None):
    prefix = ''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            print(prefix)
            print(list(args))
            print(kw)
            ret = func(*args, **kw)
            print('end call')
            return ret
        return wrapper

    if isinstance(obj, types.BuiltinFunctionType) or isinstance(obj, types.FunctionType):
        return decorator(obj)
    else:
        prefix = obj
        return decorator


@log_1('')
def exec(x, y, z, **kw):
    print('ok')


exec(1, 2, 3, name='litao')


def before(request, args):
    print('before')


def after(request, args):
    print('after')


def filter1(before_func, after_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            before_result = before_func(args, kw)
            if before_result != None:
                return before_result

            result = func()
            if result != None:
                return result

            after_result = after_func(args, kw)
            if after_result != None:
                return after_result

        return wrapper
    return decorator


@filter1(before, after)
def index():
    print('index')


index()

# partial function
int2 = functools.partial(int, base=2)

print(int2('10010101'))


# variable work area  _a __x
def _private(name):
    print(name)


def greeting():
    _private('hello world')


greeting()

# type() isinstance() dir() hasattr() getattr() setattr()
print(type(123))
print(type(OOP.Animals()))
print(isinstance(123, int))
print(isinstance(OOP.Animals(), OOP.Animals))

a = OOP.Animals()
print(dir(a))

# Enum
month = Enum('Month',('Jan','Fab','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for k, v in month.__members__.items():
    print(k, ':', v.value)
print(month.Jan.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thi = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon.value)


@unique
class Gender(Enum):
    Male = 0
    Female = 1


print(Gender.Male)


# type
def fn(self, name='world'):
    print('hello, %s' % name)


Hello = type('Hello', (object,), dict(hello=fn, att='hello'))


h = Hello()
h.hello()
h.__name = 'nihao'
print(h.__name)
print(h.att)

# metaclass magic code
t_1 = []
# t_1.add('1')

# ORM + METACLASS
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        print('<%s:%s>' % (self.__class__.__name__, self.name))


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


def eat(self):
    print('eat=...')


Foo = type('Foo', (object,), {'name': 'apple', 'eat': eat})


f = Foo()
print(f)
print(f.name)
f.eat()


Fooo = type('Fooo', (Foo,), {})


print(Fooo())
ff = Fooo()
print(ff.name)
ff.eat()


def meta_func(self, value):
    self.append(value)


class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = meta_func
        return type.__new__(cls, name, bases, attrs)


class MyList(list,metaclass=ListMetaClass):
    bar = 'lll'

    def __init__(self):
        self.name = 'ok'

    def say_hello(self):
        print('hello')


ll = MyList()
ll.add(1)
print(ll)


# metaclass 初始化类时将所用属性变为大写
class UpperClass(type):
    def __new__(cls, name, bases, attrs):
        print('cls %s' % cls)
        print(name)
        print(bases)
        print(attrs)
        attr_type = ((attr,value) for attr,value in attrs.items() if not attr.startswith('__'))
        # print(dict(attr_type))
        new_attrs = dict((attr.upper(),value) for attr, value in attr_type)
        print(new_attrs)
        return type.__new__(cls, name, bases, new_attrs)


class Book(object, metaclass=UpperClass):
    title = 'Flask with Python'

    def say_hello(self):
        print('hello')


b = Book()
print(b.TITLE)
b.SAY_HELLO()

# 用metaclass 检测不雅词语
sensitive_words = ['fuck', 'bitch', 'porn']


def word_in_str(string):
    return lambda word: word in string


def sensitive_word_detect(string):
    word_detect = filter(lambda word: word in string.lower(), sensitive_words)
    word_list = list(word_detect)
    print(word_list)
    if word_list:
        # raise NameError('sensitive word %s is detected in string %s ' % (word_list, string))
        pass
    else:
        print('I am a good boy!')


class DataDetectMetaCls(type):
    def __new__(cls, name, bases, attrs):
        sensitive_word_detect(name)
        map(sensitive_word_detect, [x for x in attrs])
        return type.__new__(cls,name,bases,attrs)


class BaseApi(metaclass=DataDetectMetaCls):
    base_name = 'api interface'


class GoodCls(BaseApi):
    pass


class FuckYou(BaseApi):
    pass


# Exception record
logging.basicConfig(filename='log.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.INFO)
try:
    10 / 0
except Exception as e:
    print(e)
    logging.exception(e)
finally:
    print('done')


class AttrTest(dict):
    name = 'score'

    def __getattr__(self, item):
        return self[item]


a = AttrTest(a=1,b=2)
print(a)
a.ke = 'f'
print(a.ke)
print('ke' in AttrTest())

# IO
# try:
#     fs = open('test_report.txt', 'r')
#     print(fs.read())
# except IOError as e:
#     print(e)
# finally:
#     if fs:
#         fs.close()

# read-mode r,rb
with open('test_report.txt', 'r', encoding='utf-8', errors='ignore') as fss:
    read_reault = fss.read(10)
    # read_reault = fss.readline()
    # read_reault = fss.readlines()
    while read_reault:
        print(read_reault)
        read_reault = fss.read(10)

# write-mode w,wb,a
with open('log.log', 'a') as f:
    f.write('\n' + time.strftime('%Y-%m-%d %H:%M:%S %p'))


from io import StringIO


str_f = StringIO()
str_f.write('hello ')
str_f.write('world')
print(str_f.getvalue())


w_str_f = StringIO('hi\nfine\nThank you!')
while True:
    s = w_str_f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO


byte_f = BytesIO()
byte_f.write('你好'.encode('utf-8'))
print(byte_f.getvalue())

w_byte_f = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')
print(w_byte_f.read())



print(os.name)
# os.uname() windows dont support this attribute.\
d = dict(os.environ)
print(d)
# print(d['CATALINA_HOME'], os.environ.get('CATALINA_HOME'))

# directory
print(os.path.abspath('.'))
print(os.path.join(os.path.abspath('.'), 'file.txt'))
# os.mkdir()
# os.rmdir()
print(os.path.split('C:\\Users\\litao\\PycharmProjects\\HeadToFirst\\file.txt'))
print(os.path.splitext('C:\\Users\\litao\\PycharmProjects\\HeadToFirst\\file.txt'))
# file
# os.rename('test_report.txt', 'new.txt')
# os.remove('')
# os.remove('')
print(os.listdir('.'))
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

with open('log.log','r') as dict_f:
    dict_word = {}
    while True:
        r_line = dict_f.readline()
        if r_line == '':
            break
        for word in r_line:
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
    for d, v in dict_word.items():
        print('word:%s count: %s' % (d, v))
    print(sum([x for x in dict_word.values()]))

with open('log.log','r') as dict_ff:
    print(len(dict_ff.read()))

# serialize pickling
import pickle


d_pick = dict(name='hello', value='world!')
# 1
pick_res = pickle.dumps(d_pick)
print(pick_res)
# 2
with open('dump.txt', 'ab') as ff:
    # ff.write(pick_res)
    pickle.dump(d_pick, ff)

with open('dump.txt', 'rb') as rf:
    b_res = rf.read()
    ddd = pickle.loads(b_res)
    print(ddd)

with open('dump.txt', 'rb') as rrf:
    dddd = pickle.load(rrf)
    print(dddd)

# Json
import json
json_d = dict(name='lili', age=30)
print(json_d)
json_str = json.dumps(json_d)
print(json_str)

un_json_d = json.loads(json_str)
print(un_json_d)


class Teacher:
    def __init__(self, name, age, marry):
        self.name = name
        self.age = age
        self.marry = marry


def tea2dict(tea):
    return {
        'name': tea.name,
        'age': tea.age,
        'marry': tea.marry
    }


print(json.dumps(Teacher('xix', 29, 1), default=tea2dict))
print(json.dumps(Teacher('xix', 29, 1), default=lambda obj:obj.__dict__))


def dict2stu(stu):
    return Teacher(stu['name'],stu['age'], stu['marry'])


print(json.loads(json.dumps(Teacher('xix', 29, 1), default=lambda obj:obj.__dict__), object_hook=dict2stu))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

# Processing Threading
print(os.getpid())
# pid = os.fork()
# windows dont have fork
# if pid == 0:
#     print('child process:%s,parent process:%s' %(os.getpid(),os.getppid()))
# else:
#     print('parent process:%s,parent process:%s'%(os.getppid(),pid))

from multiprocessing import Process
import multiprocessing


def run_proc(name):
    print('Run child process %s(%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('parent process is %s' % os.getpid())

    p = Process(target=run_proc, args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process end')
    print('cpu_count %s' % multiprocessing.cpu_count())
