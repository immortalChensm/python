'''
print(a)
print(a+"japanese")
print(a*3)
print(a[1])
print(a[:])
print(a[1:3])
print(a[1:7:2])
for i in a:
    print(i)
print("c" in a)
print([x for x in a])
print([x for x in a if x!='c'])
print(a.endswith("se"))
print(a.startswith("ch"))
print(a.find("in"))
print(a.upper())
print(a.lower())
print(a.zfill(5))
a = "chinese"

print("ese" not in a)
age = 1000
print("she age is %d"%(age))
print("she age is %(age)d"%{"age":200})
print("she has a %(friend)s"%{"friend":"boyfriend"})
print("she age is {0} and she has {1}".format("30","mobile"))
print("she age is {age} and she has {sj}".format(age=100,sj="mobile"))
print("she age is %.3f"%(3.4626))
print("she age is %(age).3f"%{"age":3.2235325})
'''

name = input("a:")
age  = input("b:")
print(name,age)