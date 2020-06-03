

class Person():

    def run(self):
        print("can run")
        print(self.__money)
    def eat(self,food):
        print("can eat"+food)

    def setMoney(self,money):
        if money <0:
            money = 0
        self.__money = money
    def getMoney(self):
        return self.__money

    def __init__(self,**kwargs):
        self.name   = kwargs['name']
        self.age    = kwargs['age']
        self.weight = kwargs['weight']
        self._height = kwargs['height']
        #私有属性  相当于PHP的private
        self.__money = kwargs['money']
        #特殊属性
        self.__age__ = kwargs['age']


'''
#print(object.__money)
object.run()
#外部无法访问私有属性
print(object.__money)
#动态添加属性
object.a = 100
print(object.a)
#object.__money
object._Person.__money = 1
print(object.getMoney())
'''
object = Person(**{"name":"jack","age":10,"height":10,"weight":20,"money":100})
print(object.getMoney())

print(object.__age__)

print(object._height)