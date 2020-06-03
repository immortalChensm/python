import os

print(os.name)
#print(os.uname()) linux support

#print(os.environ)
#print(os.environ.get('ALLUSERSPROFILE'))

#print(os.curdir)
#print(os.getcwd())
#print(os.listdir(r"E:\python"))

#os.makedirs("jackcsm")

#os.rmdir("jackcsm")

#print(os.stat("demo33.txt"))

#os.rename("demo33.txt","demo33_1.txt")

#os.remove("demo33_1.txt")

#os.system("notepad")

#print(os.system("ping www.baidu.com"))
#print(os.system("python"))

#print(os.system("write"))
#os.system("music")

#os.system("mspaint")

#os.system("msconfig")

#os.system("calc")

#print(os.system("winver"))
#print(os.system("systeminfo"))

#os.system("notepad")

#os.system("taskkill /f /im notepad.exe")

#print(os.path.abspath("./"))

#print(os.path.join(os.path.dirname(__file__),"jackcsm"))
path = r"E:\python\demo2\demo32.txt"
#print(os.path.split(path))

#print(os.path.splitext(path))

#print(os.path.isdir(path))

#print(os.path.isfile(path))

#print(os.path.exists(os.path.dirname(path)))

#print(os.path.getsize(path))

print(os.path.dirname(path))
print(os.path.basename(path))