

class Person():

    def run(self):
        print("can run")
    def eat(self,food):
        print("can eat"+food)
    def __init__(self,**kwargs):
        self.name   = kwargs['name']
        self.age    = kwargs['age']
        self.weight = kwargs['weight']
        self.height = kwargs['height']
    def __del__(self):
        print("析构函数用于释放资源")

    def __strsss__(self):
        #此方法类似PHP的__toString()方法
        return "这里是str"
    def __repr__(self):
        return "%s-%d-%d-%d"%(self.name,self.age,self.weight,self.height)

object = Person(**{"name":"jack","age":10,"height":10,"weight":20})
object.run()
print(object)

