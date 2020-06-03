from multiprocessing import Process
from time import sleep
#主进程等待所有子进程结束后再结束
def run():
    print("子进程启动")
    sleep(3)
    print("子进程结束")

if __name__ =='__main__':
    print("主进程启动")
    p = Process(target=run)
    p.start()

    p.join()#等子进程结束之后，再结束主进程
    print("主进程结束")