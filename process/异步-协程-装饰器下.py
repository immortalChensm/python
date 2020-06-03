
import threading
import time

def longio():
    print("开始耗时操作")
    time.sleep(5)
    yield "耗时操作处理完成"
    print("结束耗时操作")

def finish(data):
    print("请求a终于处理完成了")
    print("处理后的结果是"+data)

def genCoroutine(func):
    def wrapper(*args,**kwargs):
        gen1 = func()  #得到reqa生成器
        gen2 = next(gen1)#执行next之后会执行longio得到第二个生成器
        def run(g):
            res = next(g)
            try:
                gen1.send(res)
            except StopIteration as e:
                pass

        threading.Thread(target=run,args=(gen2,)).start()#开启一个线程挂起，将longio传递并执行
    return wrapper

@genCoroutine
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
    reqa()
    reqb()
if __name__=='__main__':
    main()