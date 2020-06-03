
class Human(object):
    def __init__(self,name,age,money):
        self.name = name
        self.age  = age
        self.__money = money
    def run(self):
        print("run")
    def eat(self):
        print("eat")