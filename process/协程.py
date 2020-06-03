import time,threading
def longio():
    print("网络io耗时5秒")
    time.sleep(5)
    print("网络io耗时运行完成")
    yield '耗时任务执行完成'

def genCoroutine(func):

    def wrapper(*args,**kwargs):
        gen1 = func()
        gen2 = next(gen1)

        def run(gen1, gen2):
            try:
                res = next(gen2)
                gen1.send(res)
            except StopIteration as e:
                pass

        threading.Thread(target=run, args=(gen1, gen2)).start()
    return wrapper



@genCoroutine
def reqa():
    print("我是a请求")
    res = yield longio()
    print("a请求执行完成"+res)
def reqb():
    print("我是b请求")
    print("b请求执行完成")
def main():
    reqa()
    reqb()

if __name__=='__main__':
    main()