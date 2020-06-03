
class Person():

    def __init__(self,name,age):
        self.__name = name
        self.__age  = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age

per = Person("jack",20)
print(per.name)
print(per.age)
'''
访问私有类，得添加装饰器@property peopertyname.setter
类似php拦截器 但功能好像不咋样
'''