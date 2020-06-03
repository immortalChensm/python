
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print(self.name+" eat "+food)