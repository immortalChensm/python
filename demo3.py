import redis
"""
r = redis.StrictRedis(host='127.0.0.1',port=6379,charset='utf8',decode_responses='utf8')

#print(r.keys("*"))

for key in r.keys("*"):
    #print(r.type(key))
    if r.type(key)=='string':
        print(r.get(key))
        
print(r)

print(list(r))
print(tuple(r))
print(dict(r))
r = range(10)

i = iter(r)
print(next(i))
print(next(i))
m = map(abs,(-1,0,1))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(list(map(abs,(-1,0,1))))
print(m)

print(list(m))

for line in list(m):
    print(line)
m = zip((1,2,3),('a','b','c'))

print(next(m))
m = filter(bool,['hello','jack','tony'])
print(next(m))
e = enumerate('chinesegovernment')
print(e)
print(next(e))

print(iter(e) is e)
#print(next(R))

r1 = iter(R)
print(next(r1))
print(next(r1))

r2 = iter(R)
print(next(r2))
R = range(10)

print(R)
l = map(abs,(-1,0,1))
print(l)
print(next(l))
print(iter(l) is l)




try:
    hello
except:
"""


