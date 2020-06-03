import pickle

path = r"E:\python\demo2\demo33.txt"
myList = [1,2,3,"chinese"]
f = open(path,"wb")

pickle.dump(myList,f)

f.close()

f1 = open(path,"rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()