a = '10'
print(a)
print(int(a,base=2))
#偏函数
def int2(a,base=2):
    return int(a,base)

print(int2(a))

import functools

int3 = functools.partial(int,base=2)
print(int3('1011'))