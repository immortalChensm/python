import os
import sys
"""
print(os.path) #当前python路径
print(__file__) #当前脚本完整路径
print(os.path.dirname(__file__))#得到当前文件的上层目录
print(os.path.join(os.path.dirname(__file__),'/static'))
这里__file__是个常量，可以得到当前文件的路径
os.path.dirname 是获取当前文件所在的目录
os.path.join 是将当前目录拼接 static得到一个完整的目录

os.path.join就是组装成指定的目录

a,*b = 'china'
print(a,b)

class A():
    setting = dict()
    def showmsg(self,msg):
        print(msg)
    def __init__(self,setting):
        self.setting=setting



def test(a,b,c):
    x,y,z=a,b,c
    print(x,y,z)

var = dict(a=10,b=20,c=30)
test(**var)
class Dog():
    name = '小白'



attr = getattr(Dog(),'name','name')
print(attr)
print("{0}{1}".format("china","japanese"))
print(('{0}{1}'.format("usa","japanese"),"ok"))
"""

import json

print(json.dumps())