
import threading
import time
gen = None
def longio():
    print("请求a处理中")
    def run():
        print("请求a在处理中")
        time.sleep(5)

        global gen
        gen.send("a我处理好了")
    threading.Thread(target=run).start()


    #print("请求a处理完成")

def finish(data):
    print("请求a终于处理完成了")
    print("处理后的结果是"+data)

def reqa():
    print("请求a处理中")
    res = yield longio()
    time.sleep(1)
    print("请求a处理完成"+res)

def reqb():
    print("请求b处理中")
    time.sleep(1)
    print("请求b处理完成")
def main():
    global gen
    gen = reqa()
    next(gen)
    reqb()
if __name__=='__main__':
    main()