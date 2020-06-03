class Person():

    def run(self):
        print("can run")
    def eat(self,food):
        print("can eat"+food)
    def say(self):
        #self类似JS中的this谁调用本类，就指向谁
        print("Hello,my name is %s,I am %d years old"%(self.name,self.age))

    def play(a):
        print("play"+a.name)
        #在python中方法的第一个参数是表示实例化时的对象变量，名字默认为self
    def __init__(self,**kwargs):
        self.name   = kwargs['name']
        self.age    = kwargs['age']
        self.weight = kwargs['weight']
        self.height = kwargs['height']
    def talk(self):
        print(self.__class__)#得到本类的名称
        p = self.__class__(**{"name":"jackma","age":100,"weight":5,"height":30})
        print(p.name)

data = {
    "name":"jack",
    "age":10,
    "weight":50,
    "height":190
}
object = Person(**data)
object1 = Person(**{
    "name":"tom",
    "age":20,
    "weight":60,
    "height":200
})
object1.say()
object.say()
object1.play()

object.talk()
