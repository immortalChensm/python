'''
错误异常处理
try........except..........else
程序会尝试着执行语句，当语句出现错误时会匹配到except的对应错误
如果没有就执行esle语句

'''
try:
    #print(3/0)
    print(num)
except NameError as e:
    print("不存在此变量")
except ZeroDivisionError as e:
    print("被除数不能为0")

print("*"*20)


try:
    print(5/0)
except:
    print("程序出现了异常")


try:
    print(nums)
except (NameError,ZeroDivisionError,OSError):
    print("程序出错了")