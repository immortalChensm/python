import time
def longIo():
    print("处理耗时请求")
    time.sleep(5)
    print("耗时处理完成")

    return "耗时处理返回"
def reqa():
    print("处理请求a")
    str = longIo()
    print(str)
    print("请求a处理结束")

def reqb():
    print("处理请求b")
    print("请求b处理结束")

def main():
    reqa()
    reqb()

if __name__ == '__main__':
    main()