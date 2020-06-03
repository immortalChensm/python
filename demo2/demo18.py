from collections import Iterable
from collections import Iterator
'''
可迭代对象：作用于for循环的对象list tuple set dict stirng
迭代器：next函数运行之后会得到向一个值,到最后一个没有的时候会抛出StopIteration
可迭代对象：Iterable
迭代器：Iterator
可以迭代的对象有：
1、集合类型  list tuple set string dict
2、generator 生成器和带有yield gererator function 
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance((),Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance((),Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
l = (x for x in range(5))

print(l.__next__())
a = [1,2,3,4,5]
print(a is iter)

b = iter(a)
print(b is Iterator)
print(next(b))
endstr ="end"
str = ""

for line in iter(input,endstr):
    str+=line+"\n"

print(str)
'''
from printmy import 打印

苹果=5
牛肉=10

苹果的价格=2.5
牛肉的价格=2.6

总价格=苹果*苹果的价格+牛肉*牛肉的价格
打印(总价格)
如果=if
如果 3<5:
    打印(对)





