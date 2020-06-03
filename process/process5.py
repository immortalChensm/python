from multiprocessing import Pool
import os,time,random

def run(name):
    print("子进程%d启动--%d"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end   = time.time()
    print("子进程%d结束--%.2f"%(name,end-start))

if __name__=='__main__':
    print("主进程启动")
    #创建一个进程池  进程池用一统一管理所有的子进程  参数默认是cpu的核心数量
    pp = Pool(2)
    for i in range(4):
        #创建子进程，并往进程池里添加
        pp.apply_async(run,args=(i,))

    pp.close()
    pp.join()#只有进程池里的所有子进程结束后再执行主进程的后面
    print("主进程结束")
