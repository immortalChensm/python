from csm import csmProcess


if __name__=='__main__':
    print("主进程开始")

    p = csmProcess('jackcsm')
    p.start()
    p.join()
    print("主进程结束")