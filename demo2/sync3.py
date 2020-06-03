import time
import threading
gen = None
def longIo():

   def run():
       print("处理耗时请求")
       time.sleep(5)
       global gen
       print("耗时处理完成")
       try:
           gen.send("活我已经做完了")
       except StopIteration as e:
           pass


   threading.Thread(target=run).start()

def reqa():
    print("处理请求a")
    res = yield longIo()
    print("请求a的耗时完成返回数据:",res)
    print("请求a处理结束")

def reqb():
    print("处理请求b")
    print("请求b处理结束")

def main():
    global gen
    gen = reqa()
    next(gen)
    reqb()

if __name__ == '__main__':
    main()