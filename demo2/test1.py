

# class test():
#     name = '1'
#     age = 100
#
#
#
# test = test()
# print(test.name)
#
# a = dict.fromkeys(['a','b'],100);
# print(a)
# print(a['a'])
# print(a.get('a'))

class Test(object):
    def __init__(self,a):
        self.a = a
    def check(self):
        self(100)

t = Test(2)
print(t.check())