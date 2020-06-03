from multiprocessing import Process
from time import sleep
#进程执行顺序，谁时间长就最后结束
def run():
    print("子进程启动")
    sleep(3)
    print("子进程结束")
if __name__ == '__main__':
    print("主进程启动")

    p = Process(target=run)
    p.start()

    print("主进程结束")

