
import datetime
'''
类型有
datetime
timedelta
date
time
zftone
'''
d1 = datetime.datetime.now()
d2 = datetime.datetime(1990,12,12,1,2,3,43)

d3 = d1.strftime("%Y-%m-%d %X")
print(d3)
print(type(d3))

d4 = d2.strptime(d3,"%Y-%m-%d %X")
print(d4)
print(type(d4))

d5 = datetime.datetime(1999,1,2,3,4,2,12)
d55 = datetime.datetime(1990,12,16,9,9,9,12)
d6 = datetime.datetime.now()


d7 = d6-d5
print(type(d7))
print(d7)
print(d7.days)
print(d7.seconds)
print(d7.microseconds)