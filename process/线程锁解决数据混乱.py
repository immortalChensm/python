import threading
a = 0
#线程锁
lock = threading.Lock()
#多线程锁可能会造成死锁的问题  线程锁一般会让程序处于单线程模式运行
#相当于同步，有个先后顺序，而不是并发执行

def run(num):
    global a
    print("子线程(%s)启动"%(threading.current_thread().name))
    for i in range(1000000):
        '''
        lock.acquire()#线程进来时锁住
        try:
            a = a + num
            a = a - num
        finally:
            lock.release()#当前线程执行完以后释放掉锁
        '''
        #with lock 有锁定和解锁功能
        with lock:
            a = a+num
            a = a-num

    print("子线程(%s)结束"%(threading.current_thread().name))

if __name__=='__main__':

    print("主线程启动")
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("主线程结束---%d"%(a))

