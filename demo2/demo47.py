#from demo_45_1 import sayHello as sayGood
from demo_45_1 import *

#print(sayGood())
print(sayHello())
#覆盖了模块中定义的方法
def sayHi():
    print("hihihi")

sayHi()