
'''
print("she name is %s,and her age is %d,and her father's age is %.1f"%("lingling",20,54.3243))
print("jack\n is a good\n student")
print("jack\\n is a good\\n student")
print("tomorrow i will to do somthing now time","ok",sep="\n")
print(
good
nice
bad
sad
)
print("good\tnice")
print("\\\t\\")
print(r"\\\t\\")
num1 = eval("123")
print(num1)
print(eval("+123"))
print(eval("-123"))
print(eval("13-9"))
print(eval("12+9"))
print(len("chinese"))
print("CHINESE".lower())
print("chinese".upper())

str20 = "japanese"
print(str20)
print(str20.upper())
print("CHINA is a developing country".swapcase())

print("china is a developed country".capitalize())
print("china is a developing country".title())
print(dir("ok"))
print("ok".__doc__)
print("japanese was issued army".center(50,"*"))
print("hello,chinese".ljust(40),"*")
print("america is hornor country".rjust(50,"*"))

print("9".zfill(5))
print("tom is good student".count("o"))
print("python is best language".count("python",0,len("python is best language")))
print(help("ok".count))
print("chinese there are many population live in land".find("live"))
print(help("str".find))
print("chinese and america".rfind("and"))
print("grocery there are many products are saleing".index("many"))
print("    hello,world".lstrip())
print("***********hello,world".lstrip("*"))
print("hello,world*********************".rstrip("*"),"*")
print("*************hello,world*****************".strip("*"))
print(help("str".strip))

for func in dir("str"):
    print(func)
'''

print("china".translate("中国"))
print(help("str".translate))
