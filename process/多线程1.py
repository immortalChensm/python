import threading,os,time
a = 0
def run(num):
    print("子线程(%s)启动"%(threading.current_thread().name))
    global a
    for i in range(1000000):
        a = a+num
        print(a)
        a = a-num
        print(a)
    print(a)
    print("子线程(%s)结束"%(threading.current_thread().name))

if __name__=='__main__':
    print("主线程启动%s"%(threading.current_thread().name))

    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("主线程(%s)结束--%d"%(threading.current_thread().name,a))
