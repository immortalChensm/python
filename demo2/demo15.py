
'''

t = tuple()
print(t)
t1 = (1,2,3)
print(t1)

t2 = (1,2,3,(4,5,6))
print(t2)

t3 = (1,2,3)+(4,5,6)
print(t3)
print(t1[0])
print(t1[-1])
print(1 in t1)
for x in t1:
    print(x)
print(x for x in t1)
print(t1[0:-1:1])
print(dir(t1))
print(help(t1.count))
print(t1.count('b'))
print(help(t1.index))
t1 = ('a','b','c','b')
print(t1.index('b'))

str1 = "china is developed country"
print(str1.split(" "))
str1 = """
china is a developed country
china is big country
china is a strong country
"""
print(str1.splitlines())
print(dir("str"))
list1 = ['she','is','good','student']
print("".join(list1))
str1 = "these days we can learn english on app and many website,for example,u can storage your english words in the web server"

print(str1.replace("english","中文",1))
str1 = str.maketrans("ab","中国")
str2 = "ab is good country"
str3 = str2.translate(str1)
print(str3)
str1 = "looking for a woman"
print(str1.encode())

data2 = str1.encode()
print(data2.decode())
str1 = "lsjklfdf"
print(str1.isalpha())
print(str1.isalnum())
print(str1.isnumeric())
print(str1.isdecimal())
print(str1.isdigit())
'''


str1= "abc"
print(str1.isupper())
print("ABC".isupper())
print("ABC1".isupper())
print("ABC#".isupper())
print("1".isupper())




