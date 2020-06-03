"""
函数，有a,b形式参数
在调用的时候，传递了一个数值和一个列表
在执行本函数的时候分别修改了他们的值，相当于引用传递
python,js效果均一致
php 则无法修改
def change(a,b):
    a=2
    b[0] = 'spam'



x=1
y=[1,2]
change(x,y)
print(x,y)
x = 1
a=x
a=2
print(a,x)
l = [1,2]
b=l
b[0]='spam'
print(l,b)
def change(a,b):
    a=1
    b[0]='spam'


x=2
y=[1,2]
change(x,y[:])#阻止传递的参数发生改变
print(x,y)#阻止传入的参数发生改变
def change(a,b):
    a=1
    b=b[:]
    b[0]='chinese'


x=2
y=[1,2]
change(x,y)
print(x,y)
def multiple(a,b):
    a=2
    b=[3,4]
    return a,b

x=1
y=[1,2]
x,y=multiple(x,y)
print(x,y)

def f(a,b,c):
    print(a,b,c)


f(1,2,3)#按位置传递  按位置匹配
f(c=1,b=2,a=3)#关键字参数  按变量名匹配
f(1,c=2,b=3)
def f(a,b=2,c=3):
    print(a,b,c)


f(1)
f(2)
f(a=3)
f(a=3,b=5)
def func(spam,eggs,torst=0,ham=0):
    print((spam,eggs,torst,ham))


func(1,2)
func(1,ham=2,eggs=3)
func(spam=2,eggs=4,ham=4)
func(1,2,3,4)
def f(*args):
    print(args)


f(1)
f(1,2,3)
f('chinese','japanese','korea')
#默认参数

def f(**args):
    print(args)


f()
f(a=1,b=2)
func(1)
func(1,2,3)
func(1,2,3,x=1,y=2)
def func(a,*pargs,**kargs):
    print(a,pargs,kargs)


func(1,2,3,x=1,y=3)
def f(a,b,c,d):
    print(a,b,c,d)


args = (1,2)
args+=(3,4)
f(*args)
args={'a':1,'b':2}
args['c'] = '3'
args['d'] = '4'
f(**args)
f(*(1,2),**{'c':1,'d':2})

f(1,*(2,3),**{'d':4})

f(1,c=3,*(2,),**{'d':4})

f(1,*(2,3),d=4)

f(1,*(2,c),c=3,**{'d':4})


def f(a,b,c,d):
    print(a,b,c,d)




f(1,*(2,3),**{'d':4})
f(1,*(2,),c=3,**{'d':4})
f(1,*(2,),c=3,**{'d':4})

f(1,**{'b':2},c=3,*(4))

def f(*args):
    print(args)


f(1)
f(1,2,3,4)
f('chines','japanese','america')
def f(**args):
    print(args)


f(a='b',c='d')
#解包参数

def f(a,b,c,d):
    print(a,b,c,d)


a = (1,2)
a+=(3,4)
f(*a)
trancer 传递的参数类型是收集参数，收集多个参数
func 传递的参数类型是解包参数，即传递一个参数解成多个值
def trancer(func,*pargs,**kargs):
    print("call function",func.__name__)
    return func(*pargs,**kargs)


def func(a,b,c,d):
    return a+b+c+d


print(trancer(func,1,2,c=3,d=4))
"""

def f(a,*b,c):
    print(a,b,c)

f(1,2,c=3)
f(a=1,c=3)
f(1,2,3)