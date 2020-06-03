from types import MethodType
class Person(object):
    #限制此类能添加的成员
    __slots__ = ("name","talk")


per = Person()
per.name = 'jack'
def say(self):
    print("my name is "+self.name)


per.talk = MethodType(say,per)
per.talk()
'''
per.age = '2'
def say(self):
    print("my name is"+self.age)



per.talk = say
per.talk(per)
'''

per.sex = 'female'
