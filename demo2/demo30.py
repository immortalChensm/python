

path = r"E:\python\demo2\demo32.txt"

with open(path,"wb") as f1:
    str ="jackcsm is good"
    f1.write(str.encode("utf-8"))

with open(path,"rb") as f2:
    data = f2.read()

    print(data)