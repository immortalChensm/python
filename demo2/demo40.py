'''

时间的表现形式
时间戳 time.time()
元组   time.gtime() time.localtime()
字符串  time.asctime()
'''

import time


c = time.time()
print(c)

t = time.gmtime(c)
print(t)

l = time.localtime(c)
print(l)


m = time.mktime(l)
print(m)

s = time.asctime(l)
print(s)

p = time.ctime(c)
print(p)

print(time.strftime('%Y-%m-%d %H:%M:%S'))

print(time.strftime("%Y-%m-%d %X",time.localtime(time.time())))

print(time.clock())

time.sleep(2)

print(time.clock())