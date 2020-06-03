

#文件编码和解码以二进制码保存

path = r"E:\python\demo2\demo31.txt"
'''
with open(path,"wb") as f1:
    str ="jackcsm is good man"
    f1.write(str.encode("utf-8"))
'''

with open(path,"rb") as f2:
    data = f2.read()
    print(data)

    print(type(data))

    newdata = data.decode("utf-8")
    print(newdata)
    print(type(newdata))
