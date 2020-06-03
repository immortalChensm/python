
'''

sum = 0
num = 1
while num<=100:
    sum+=num
    num+=1

print("sum=%d"%(sum))
strs = "chinese is good worker in this world"
index = 0
while index<len(strs):
    print("index=%d,str=%s"%(index,strs[index]))
    index+=1

print("aaa"<"bbb")
print(ord("a"))
print(ord("b"))
print("baacc"<"baaww")
print("A"<"a")
a ="jlsdjfklsdjflsdfjkldsfjdslfio3u32io423ij"
start = a[0]
end = 0
index = 0
while index<9999:
    if a[index]:
        end = index
    else:
        pass
    index+=1

print(end)
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)
print(list2*3)
for item in dir(list):
    print(item)
    list1.append(4)
list1.extend([5,6,7])
print(list1)
list1.insert(2,500)
print(list1)
list1.pop()
print(list1)
list1.extend([4,5,6,7])
list1.pop(4)
print(list1)
print(list1.pop(1))
print(list1.remove(2))
print(list1)

print(list1.index(2))
print(max(list1))
print(min(list1))
print(any(list1))
print(list1.count(2))
print(all(list1))
list1 = [1,2,3,2,3,2,0]
all = list1.count(2)
num = 0
while num<all:
    list1.remove(2)
    num+=1

print(list1)
list1 = [1,2,3,4,5]
list2 = list1

print(id(list1))
print(id(list2))

list2[2]= 300
print(list2)
print(list1)
list1 = [1,2,3,4,5]
list2 = list1.copy() #深度拷备 变量1和变量2拥有独立的内存空间各自指向自己的堆栈空间
list2[2] = 300
print(list1)
print(list2)
print(id(list1))
print(id(list2))
num = 0
listNum = list()
while num<10:
    val = int(input())
    listNum.append(val)
    num+=1
#print(listNum)
max = max(listNum)
all = listNum.count(max)
i = 0
while i<all:
    listNum.remove(max)
    i+=1
print(listNum)
print(max(listNum))
list1 = [1,2,3,4,5,5]

while start<end:
    tempa = list1[start]
    if list1[start+1]:
        tempb = list1[start+1]

    if tempa < tempb:
        max = tempb

    start+=1

print(max)
'''



def Mymax(list1):
    list1.sort()
    start = 0
    end = list1[-1]
    max = 0
    while start < end:
        tempa = list1[start]
        if list1[start + 1]:
            tempb = list1[start + 1]

        if tempa < tempb:
            max = tempb

        start += 1
    


