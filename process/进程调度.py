import threading,time
#线程条件对象
cond = threading.Condition()

def run1():
    with cond:
        for i in range(0,10,2):
            print("线程%s--%d"%(threading.current_thread().name,i))
            time.sleep(1)#执行一次之后
            cond.wait()#等下一个线程
            cond.notify()#告诉下一个线程我执行完成
def run2():
    with cond:
        for i in range(1,10,2):
            print("线程%s--%d"%(threading.current_thread().name,i))
            time.sleep(1)#执行一次之后
            cond.notify()#告诉下一个线程，我执行完了
            cond.wait()#然后再等下一个线程的通知

if __name__=='__main__':
    threading.Thread(target=run1).start()
    threading.Thread(target=run2).start()