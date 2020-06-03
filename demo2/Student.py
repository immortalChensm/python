from Human import Human
class Student(Human):
    def __init__(self,name,age,money):
        super(Student,self).__init__(name,age,money)

    def eatfood(self):
        self.eat()
    def getMoney(self):
        return self.__money