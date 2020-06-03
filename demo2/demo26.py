

path = r"E:\python\demo2\demo26.txt"

#f = open(path,"r",encoding="utf8",errors="ignore")
f = open(path,"r")

#str = f.read()
#print(str)

#str2 = f.read(20)
'''
str3 = f.readline()
print(str3)
str4 = f.readline()
print(str4)
str5 = f.readlines()
print(str5)
str6 = f.readlines(14)
print(str6)
str7 = f.read()
print(str7)
print("******************************")
f.seek(0)
str8 = f.read()
print(str8)
'''




f.close()

try:
    f1 = open(path,"r",encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()


print("-"*30)
with open(path,"r",encoding="utf-8") as f2:
    print(f2.read())