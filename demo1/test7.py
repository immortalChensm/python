"""
class A():
    def show(self,message):
        print(message)

class B(A):
    def show(self,message):
        A.show(self,message)



B().show('hello,python')
class A():
    def __init__(self,message):
        print(message)

class B(A):
    def __init__(self,message):
        A.__init__(self,message)


B('ok,python')
"""
class A():
    def __init__(self,message):
        print(message)


class B(A):
    def __init__(self,message):
        super(B,self).__init__(message)



B("hi,python")