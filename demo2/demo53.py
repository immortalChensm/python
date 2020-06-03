

class Person():

    name = ""
    age  = 0
    height = 0
    weight = 0

    def run(self):
        print("can run")
    def eat(self,food):
        print("eat"+food)
    def sleep(self):
        print("can sleep")
    def dosomething(self):
        print("i can to do something")


object = Person()
object.name = "jack"
object.age  = 18
object.height = 190
object.weight = 80

object.dosomething()

print(object.name,object.age,object.height,object.weight)