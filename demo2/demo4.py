'''

age = 18
age = 28
del age
age = "good"
print(type(age))
print(age)
print(id(age))
num1,num2 = 1,2
print(num1,num2)
print(id(num1),id(num2))
f1 = 1.1
f2 = 2.2
print(f1 + f2)
print(int("123"))
print(int(1.23))
print(float(1))
print(int("abc"))
print(0b0101)# 4+1
print(0o123)
print(0x12)
print(bin(1))
print(oct(1))
print(hex(12))
import fractions

print(fractions.Fraction(1,3))
print(fractions.__doc__)
print(min(1,2,3))
print(max(1,2,3))

print(abs(-2))
print(pow(2,3))
print(ascii('a'))
import math
print(math.ceil(12.1))
print(math.floor(12.9))
print(math.modf(12))
import random

print(random.choice([1,2,3]))
print(random.random())
print(random.randint(1,99))
print(random.randrange(1,10))
print(random.randrange(1,100,2))
l = [1,2,3,4,5]
random.shuffle(l)
print(l)
'''

import random
print(random.uniform(3,9))