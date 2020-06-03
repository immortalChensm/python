
'''

def show(msg,age):
    print(msg,age)

show('jack',50)
show('tony')
def show(name,age):
    return name,age
res = show("jack",60)
print(res)
l1 = [1,2,3,4,5]
l2 = l1
l2[0] = 100
print(l1)

l3 = l1.copy()

l3[0] = 1000
print(l1)
a = 10
b = 10
print(id(a),id(b))
b = 20
print(a,b)
print(id(a),id(b))

在python中，变量存数据，其实并不是直接保存的数据
而是将存储数据的地址！！！
当多个变量存储的数据完全一致时，就会同时指向这个数据的内存地址
当你在修改某个的时候如以下示例
a = 10
b =10
变量a和变量b他们存储的数据都是一样的，都是10，其指向的内存地址是一样的
假设变量b=20了，此时变量b就会指向20的内存地址，并不会去修改变量a的数据

a = 'a'
b = 'a'
print(a,b)
print(id(a),id(b))
b = 'b'
print(a,b)
print(id(a),id(b))
def show(name,age):
    print(name,age)

show(age=18,name='tony is')
def show(name="jack is",age=18):
    print(name,age)

show()
show("tony",20)

def show(name,*arg):
    print(name)
    for x in arg:
        print(x)


show("jack","good","best","nice")
def show(name,**args):
    print(name)
    for x in args.keys():
        print(x,args[x])

show("jack",age=100,height=300,size=50)
def show(name,size,age,sex):
    print(name,size,age,sex)

l = [30,30,1]
def show(*args,**kwargs):
    for x in args:
        print(x)

    for y in kwargs:
        print(y)

show(1,2,3,4,5,name='jack',age=100,size=400)
sum = lambda num1,num2:num1+num2
def func1():
    print("jackcsm is a english teacher")

def outer(func):
    def inner():
        print("*"*20)
        func()
    return inner;

f = outer(func1)

f()

print(sum(1,22))
'''





def outer(func):
    def inner(age):
        if age<0:
            age=0
        func(age)
    return inner

@outer#装饰器  用outer函数装饰say函数相当于say=outer(say) 将此函数当作参数传递给outer函数，并返回处理好的函数
def say(age):
    print("jack is %d years old"%(age))

say(-10)

#say = outer(say)
say(-10)










