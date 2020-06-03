
class Person(object):
    name = ""
    age  = 0
    height = 0
    weight = 0

    def run(self):
        print("i can run")
    def eat(self,food):
        print("i can eat"+food)


tony = Person()
print(tony)
tom  = Person()
print(tom)
jack = Person
print(jack)
tom.run()
jack().run()
a = 0x55
b = 0xaa
print(a|b)