import threading,time


def run(num):
    print("子线程启动%s"%(threading.current_thread().name))

    time.sleep(2)
    print("hello,world")
    time.sleep(2)
    print(num)
    print("子线程结束%s"%(threading.current_thread().name))

if __name__=='__main__':
    print("主线程启动%s"%(threading.current_thread().name))
    #target=要运行的代码如函数 name="rootThread"子线程的名字  args线程的参数
    t = threading.Thread(target=run,args=(1,))
    t.start()
    t.join()#等待子线程结束以后再执行主线程的
    print("主线程结束%s"%(threading.current_thread().name))