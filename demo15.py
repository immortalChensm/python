
"""
def fab(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1


fab(5)

a = enumerate('chinese')
print(next(a))
a = iter("chinese")
for b in a:
    print(b)
    class Fab(object):
    def __init__(self,max):
        self.max=max
        self.n,self.a,self.b=0,0,1
    def __iter__(self):
        return self
    def next(self):
        if self.n<self.max:
            r = self.b
            self.a,self.b=self.b,self.a+self.b
            self.n=self.n+1
            return r
        raise StopIteration()


for a in Fab(5):
    print(a)
"""

def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1


for n in fab(5):
    print(n)


print(fab(5))

b = fab(5)
print(next(b))
print(b.__next__())