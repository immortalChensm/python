'''
print(10)
print(10 + 8)
print("hello ni hao","do u know")
print("10 + 8 = ",18)
'''

import random
str = ""
for i in range(6):
    str+= chr(random.randrange(ord('0'),ord('9')+1))

print(str)