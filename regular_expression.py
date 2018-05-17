# _*_ coding:utf-8 _*_
import re


# match
pattern = r'^\d{3}-\d{3,8}$'
val = re.match(pattern, '010-01234569')
if val:
    print('ok')
    print(val.group(0))
else:
    print('fail')

# split
string = 'a b c   d'
print(string.find('b'))
print(re.split(r'[\s]+', string))
string1 = 'a,b, c  d'
print(re.split(r'[\,\s]+', string1))
string2 = 'a,b c ,;;;d  e;'
print(re.split(r'[\s\,\;]+', string2))

# group
p1 = r'^(\d{3})-(\d{0,8})$'
res1 = re.match(p1, '010-01234567')
if res1:
    print('ok')
    m1 = res1.group(0)
    print(m1)
    m2 = res1.group(1)
    print(m2)
    m3 = res1.group(2)
    print(m3)
    print(res1.groups())
else:
    print('fail')

t_pattern = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])'
print(re.match(t_pattern, '19:36:00').groups())

# greedy
greedy_pattern = r'^(\d*?)(0*)$'
print(re.match(greedy_pattern, '102300').groups())

# 预编译正则表达式 compile
re_com = re.compile(p1)
print(re_com.match('010-01234567').groups())

# search()
# 原子 \n \t \s \w \d
pa = '\w\dpython\w'
string_n = 'dafd3456pythony_df'
sea = re.search(pa, string_n)
print(sea.group(0))

pa1 = '[^xyz]py'
string_11 = 'xzapython'
print(re.search(pa1, string_11))
