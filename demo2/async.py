import time
import threading
def longIo(callbank):

    def run(cb):
        print("处理耗时请求")
        time.sleep(5)
        print("耗时处理完成")
        cb("这件事我已经做完了")
    threading.Thread(target=run,args=(callbank,)).start()

def finish(data):
    print("异步请求处理完成，返回的数据是：",data)
def reqa():
    print("处理请求a")
    longIo(finish)
    print("请求a处理结束")

def reqb():
    print("处理请求b")
    print("请求b处理结束")

def main():
    reqa()
    reqb()

if __name__ == '__main__':
    main()