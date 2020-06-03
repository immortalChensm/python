from multiprocessing import Process
from time import sleep
import os
'''
多进程：进程是程序的一个实例
多进程就是cpu轮流的快速运行，可以实现多任务机制
'''
def run(str):
    while True:
        print("jackcsm is %s boss---%s----%s"%(str,os.getpid(),os.getppid()))
        sleep(1.5)

if __name__ == '__main__':
    #当前在正在运行的程序为主进程
    #在此开启一个子进程
    print("这里是主进程，进程号为：%s"%(os.getpid()))
    p = Process(target=run,args=('big',))#指定子进程要运行的方法
    p.start()#子进程启动

    while True:
        print("tony are from usa")
        sleep(1)

    #run()