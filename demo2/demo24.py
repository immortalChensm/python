

try:
    print(1/0)
except ZeroDivisionError as e:
    print("又出错了哦")
finally:
    print("不管咋样都要执行我这里的")