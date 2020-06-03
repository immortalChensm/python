import pymysql
"""
db = pymysql.connect('localhost','root','','python',charset='utf8')

cursor = db.cursor()


try:
    cursor.execute('show tables')
    # print(cursor.fetchall())

    cursor.execute("select * from p1")
    #print(cursor.fetchall())

    for id,name,sort in cursor.fetchall():
        print(id,name,sort,end='\n')
except:
    print('fatal error:'+db.DataError)
l1 = [1,2,3,4]
l2 = [5,6,7,8]

print(zip(l1,l2))
print(list(zip(l1,l2)))

for x,y in list(zip(l1,l2)):
    print(x,y,x+y,end='\n')
    s1 = 'abc'
s2 ='xyz123'

print(map(s1,s2))
print(map(None,s1,s2))

for x in map(None,s1,s2):
    print(x)
    print(map(ord,'spam'))
#获取spam字符串对应的ascii码
print(list(map(ord,'spam')))
for x in list(map(ord,'spam')):
    print(x,end='\n')
    print(ord('a'))
    a = []
for c in 'spam':
    a.append(ord(c))


print(a)
keys = ['a','b','c']
vals = [1,2,3]
d = {}
for (k,v) in list(zip(keys,vals)):
    d[k] = v


print(d)
keys = ['japanese','chinese','america']
vals = [10,99999,88]

print(dict(zip(keys,vals)))
for x in [1,2,3,4]:
    printx)
    for x in (1,2,3,4,5):
    print(x,sep=',',end='')
    for x in 'python':
    print(x,end='')
    for x in dir(sys):
    print(x,help(x))
    sys.stdout.write('hello')
    import sys

sys.stderr.write('你的程序出错了');
import sys

def print_r(info,sep=''):
    sys.stdout.write(info+sep)


print_r('hi')
f = open("demo2.txt","w")
f.write("hi\n")
f.write("hello\n")
f.write("world\n")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print("-------------------------------\n")
print(f.read())
print("---------------------------------\n")
print(f.readlines())
print(f.readlines())
print(f.read())
print(help(f.readlines))
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
f = open("demo2.txt","r")
for line in open("demo2.txt"):
    print(line,end='')
    f = open("demo2.txt","r")
print(next(f))
print(next(f))
print(next(f))
print(next(f))
s = ['a','b','c','d']
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
f = open("demo2.txt","r")
print(iter(f) is f)
print(f.__next__())
print(next(f))

l1 = ['a','b','c']
print(iter(l1) is l1)
print(next(l1))
import os
print(os.popen("dir"))
dir = os.popen("dir")

for line in dir:
    print(line)

print(os.popen("time"))

for line in os.popen("time"):
    print(line)
    php = os.popen("php E:\wwww\demo\demo2.php start")

for line in php:
    print(line)
    r = range(5)

i = iter(r)

print(next(i))
print(next(i))
import os
print(e)
print(iter(e) is e)
for (k,v) in list(enumerate('chinese')):
    print(k,v)
    e  = enumerate('chinese')

print(next(e))
i = enumerate('123456789')

for x in i:
    print(x)
print([x+y for x in ['a','b','c'] for y in ['x','y','z']])
res = []

for x in ['a','b','c']:
    for y in ['1','2','c']:
        res.append(x+y)


print(res)
print([line for line in open("demo2.txt")])
print([line.upper() for line in open("demo2.txt")])
print(list(map(str.upper,open("demo2.txt"))))
print('hi\n' in open("demo2.txt"))
print(sorted(open("demo2.txt")))
print(list(map(str.upper,open("demo2.txt"))))
print(list(zip([1,2,3],['a','b','c'])))
print(list(enumerate(open("demo2.txt"))))
print(list(filter(bool,open("demo2.txt"))))
import functools,operator

print(functools.reduce(operator.add,open("demo2.txt")))
迭代器
文件迭代器
iter迭代器
enumiterator迭代器
shell 命令迭代器
迭代器有个共同点
都支持next函数或是__next()__
输出的结果大多是列表
列表解析
可扩展的列表解析
产生列表的函数
list
zip
enumiterator
filter
map
functiontools,operato
print(list('chinese'))
print(list([1,2,3]))
print(list(open("demo2.txt")))
print(list(map(str.upper,'chinese')))
print(list(map(str.upper,['a','b','c'])))
print(list(map(str.upper,open("demo2.txt"))))
print(list(map(str.upper,{'a':'aa','b':'bb'})))
print(list(map(str.upper,('a','b','c'))))
print(list(iter('chinese')))
print(list(iter(['a','b','c','d'])))
print(list())
print(enumerate('chinese'))
print(list(enumerate('chinese')))
print(filter(bool,'chinese'))
print(list(filter(bool,'chinese')))
import functools,operator

print(functools.reduce(operator.add,'chinese'))
print(list(functools.reduce(operator.add,'chinese')))
print(sum([1,2,3,4,5]))
print(any(['a','b']))
print(all(['b','c']))
print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))
print(list(open("demo2.txt")))

print(iter(open("demo2.txt")) is open("demo2.txt"))
print(tuple(open("demo2.txt")))
print('&&'.join(open("demo2.txt")))
a,b,c = open("demo2.txt")
print(a,b,c)
a,*b,c = open("demo2.txt")

print(a,b,c)
.*a = open("demo2.txt")
print(a)

"""





import os

print(os.path)