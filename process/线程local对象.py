'''
线程锁用于解决线程并发执行时造成的数据混乱
theading.Local也可以处理
2018-06-30 星期六

'''
import threading

num = 0
local = threading.local()

def run(x,n):
    x = x+n
    x = x-n
def func(n):
    local.x = num
    for i in range(1000000):
        run(local.x,n)

    print("子线程(%s)的结果是%d"%(threading.current_thread().name,num))
if __name__=='__main__':
    print("主线程启动")
    t1 = threading.Thread(target=func,args=(6,))
    t2 = threading.Thread(target=func,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("主线程结束---%d"%(num))