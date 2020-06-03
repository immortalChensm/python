
import threading
import time
def longio(callback):
    print("请求a处理中")
    def run(cbk):
        print("请求a在处理中")
        time.sleep(5)
        cbk("我处理完了哦")

    threading.Thread(target=run,args=(callback,)).start()


    #print("请求a处理完成")

def finish(data):
    print("请求a终于处理完成了")
    print("处理后的结果是"+data)

def reqa():
    print("请求a处理中")
    longio(finish)
    time.sleep(1)
    print("请求a处理完成")

def reqb():
    print("请求b处理中")
    time.sleep(1)
    print("请求b处理完成")

if __name__=='__main__':
    reqa()
    reqb()