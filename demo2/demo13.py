

'''
for x in range(1,10,2):
    print(x)

for (k,v) in enumerate(range(10)):
    print(k,v)
    print(n.__next__())
print(next(n))
'''

n = iter("chinese")
for x in n:
    print(x)