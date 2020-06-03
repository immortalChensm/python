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


object = Person(**{"name":"jack","age":10,"height":10,"weight":20})
object.run()
#手动释放对象
del object
#释放的对象无法再使用了
#print(object.name)

def func1():
    p = Person(**{"name":"tom","age":1,"height":2,"weight":3})

func1()#函数执行完毕后，会自动释放
while 1:
    pass


