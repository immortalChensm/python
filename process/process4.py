from multiprocessing import Process
from time import sleep
#进程间的变量无法共享
num = 100
def run():
    print("子进程")
    global num
    num+=1

if __name__=='__main__':
    print("主进程")
    p = Process(target=run)
    p.start() #启动子进程
    p.join() #等子进程结束后再执行后面的语句
    print("主进程的结果---%d"%num)