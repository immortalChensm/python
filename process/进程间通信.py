
from multiprocessing import Process,Queue
import os,time

def write(q):
    print("子进程写开始%d"%(os.getpid()))

    for chr in ['A','B','C','D']:
        q.put(chr)
        time.sleep(1)
    print("子进程写结束")

def read(q):
    print("子进程读开始%d"%(os.getpid()))

    while True:
        value = q.get(True)
        print("value="+value)

    print("子进程读结束")

if __name__=='__main__':
    print("主进程启动")
    #创建一个列队
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()

    pw.join()#写子进程结束
    pr.terminate()#读子进程中断  因为读子进程内有循环无法结束，只能强行中止
    print("主进程结束")
