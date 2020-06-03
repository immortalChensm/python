'''

from time import *
print(time())
sleep(2)
print(mktime(localtime(time())))
import demo_45_1 as demo
demo.sayHello()
print(demo.__doc__)
'''

import demo_45_1 as demo

demo.sayHello()