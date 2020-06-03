
'''
协程：类似中断 中断的原因是主程序运行时，发生中断请求，响应中断，中断返回，再执行原来的地方
'''
def a():
    print("1")
    yield 10
    print("2")
    yield 20
    print("3")
    yield 30
m = a()
print(m)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
