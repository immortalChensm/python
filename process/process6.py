from multiprocessing import Pool
import os,time,random
import requests
def run1(name):
    print("【耗时】子进程%d启动---%d"%(os.getpid(),name))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("【耗时】子进程%d结束--耗时%.2f"%(os.getpid(),end-start))
def run2():
    print("【百度】子进程启动---%d"%(os.getpid()))
    url = "http://www.baidu.com"
    response = requests.get(url)
    print(response.text)
    print("【百度】子进程结束%d"%(os.getpid()))
def run3():
    print("子进程开始%d"%(os.getpid()))
    print("只打印一句话")
    print("子进程结束%d" %(os.getpid()))

if __name__=='__main__':
    print("主进程启动")
    process = [run1,run2,run3]

    pp = Pool(2)
    #for i in process:
     #   pp.apply_async(i,args=(6,))
    pp.apply_async(run1,args=(6,))
    pp.apply_async(run2)
    pp.apply_async(run3)
    pp.close()
    pp.join()
    print("主进程结束")