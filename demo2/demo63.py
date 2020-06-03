
class Person(object):

    name = "person"#类本类属性
    def __init__(self,name):
        #self为实例化时的对象
        #name为对象属性
        self.name = name
    def hello(self):
        print("hello,world")

#类属性  类名：属性类似PHP静态类调用
print(Person.name)
Person.hello(Person)

per = Person("tom")
per.hello()

'''
python具有php特点，不用实例化类，都可以直接调用类的成员
print(Person.name)
Person.hello(Person)

per = Person("tom")
per.hello()

python具有js类似功能，可以给对象添加成员属性和成员 方法
per.age = 100
def sayage():
    print("i am 18")
per.sayage = sayage
per.sayage()

print(per.name)#调用对象属性
del per.name#对象属性删除
print(per.name)#先找对象是否存在此属性，后找类属性
print(per.name)
print(Person.name)

per.age = 100
print(per.age)
per1 = Person("jack")
print(per1.age)
def say():
    print("hello,world")
per.say = say

per.say()
'''

