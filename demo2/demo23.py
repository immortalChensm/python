
'''
BaseException 为所有异步类的基类即父类，如果写在前面，则会捕获所有的异步类，包括子类

try:
    print(1/0)
except BaseException as e:
    print("异常1")
except ZeroDivisionError as e:
    print("异常2")
'''


def func1(num):
    print(1/num)
def func2(num):
    func1(num)
def main():
    func2(0)



try:
    main()
except ZeroDivisionError as e:
    print("程序异常")

