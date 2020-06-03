class Person():

    def run(self):
        print("can run")
    def eat(self,food):
        print("can eat"+food)
    def say(self):
        #self类似JS中的this谁调用本类，就指向谁
        print("Hello,my name is %s,I am %d years old"%(self.name,self.age))
    def __init__(self,**kwargs):
        self.name   = kwargs['name']
        self.age    = kwargs['age']
        self.weight = kwargs['weight']
        self.height = kwargs['height']

data = {
    "name":"jack",
    "age":10,
    "weight":50,
    "height":190
}
object = Person(**data)
print(object)
print(object.name)
print(object.age)
print(object.weight)
print(object.height)

