# _*_ coding:utf-8 _*_
from types import MethodType


class Student(object):
    count = 0

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        Student.count += 1

    def get_name(self):
        print(self.__name)

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        print(self.__score)

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be int type')
        if score <= 0 or score >= 100:
            raise ValueError('score must bewteen 0-100')
        self.__score = score

    def print_score(self):
        print('%s grade is %s' % (self.__name, self.__score))

    def get_grage(self):
        if self.__score >= 90:
            print('A')
        else:
            print('B')



class Animals():
    def run(self):
        print('Animal is running... ')


class Dog(Animals):
    def run(self):
        print('Dog is running... ')
    pass


class Cat(Animals):
    def run(self):
        print('Cat is running... ')
    pass


d = Dog()
d.run()
c = Cat()
c.run()

print(isinstance(d, Dog))


def run_twice(animal):
    animal.run()


class Timer:
    def run(self):
        print('timer is running... ')


a = Animals()
run_twice(a)
run_twice(d)
run_twice(Timer())

print(Student.count)
s1 = Student('d', 12)
print(Student.count)
s2 = Student('s', 12)
print(Student.count)

s = Student('lucy', 60)
s.print_score()
s.get_grage()
s.age = 60
print(s.age)
# print(s._Student__name)


# slots
class Teacher:
    def __init__(self):
        print('teacher')


t = Teacher()
t.name = 'yangzhi'
print(t.name)


def set_age(self, age):
    self.age = age


t.set_age = MethodType(set_age, t)
t.set_age(24)
print(t.age)

Teacher.set_age = set_age
t1 = Teacher()
t1.set_age(12)
print(t1.age)


class Leader():
    __slots__ = ('name', 'age')
    pass


l = Leader()
l.age = 25
print(l.age)
# l.score = 23

# @Property
ss = Student('Michal', 99)
ss.set_score(90)
ss.get_score()
# ss.set_score('09')
ss.set_score(80)


class Person:
    def __init__(self):
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val):
        self.__score = val


p = Person()
p.score = 60
print(p.score)


class Screen:
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,val):
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,val):
        self.__height = val

    @property
    def resolution(self):
        return self.__height * self.__width


s = Screen()
s.height = 768
s.width = 1024

print(s.resolution)


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable:
    def run(self):
        print('running...')


class Flyable:
    def fly(self):
        print('flying...')


class Bat(Bird, Flyable):
    def say(self):
        print('hello')
    pass


class Turtle(Mammal, Runnable):
    pass


class NoteBook:
    __slots__ = ('name', 'weight', 'a', 'b')

    def __init__(self):
        self.weight = 90
        self.a = 0
        self.b = 1

    def __len__(self):
        return 100

    def __str__(self):
        return 'NoteBook'

    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            for x in range(n):
                self.a, self.b = self.b, self.a + self.b
            return self.a
        if isinstance(n, slice):
            start = n.start
            end = n.stop
            if start is None:
                start = 0
            L = []
            for x in range(end):
                if x >= start:
                    L.append(self.a)
                self.a, self.b = self.b, self.a + self.b
            return L

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25
        raise AttributeError('no attribute %s' % item)


n = NoteBook()
print(len(n))
print(n)
# for k in n:
#     print(k)

print(n[1])
print(n[2:15])
print(n.score)
print(n.age())
# print(n.location)


# rest api ? 带参数的api __getattr__ __call__
class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, item):
        if item == 'users':
            return lambda x, y: Chain('%s/%s/%s/%s' % (self.__path, item, x, y))
        return Chain('%s/%s' % (self.__path,item))

    def __str__(self):
        return self.__path

    __repr__ = __str__


c = Chain()
print(c.users('hh','yy').bin)


class Car:
    def __init__(self):
        print('i am a car.')

    def __call__(self, *args, **kwargs):
        print('hello car',args)


car = Car()
car('he')


class Model(dict):
    def __init__(self, **kw):
        # super(Model, self).__init__(self, **kw)
        print(kw)


class User(Model):
    idd = 1
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        print('subclass class')


u = User(age=1,name='litao')

class Course:
    name = 'math'
    def __init__(self,count,week):
        self.count = count
        self.week = week


cor = Course(2,1)
print(cor.name)
print(cor.count)
