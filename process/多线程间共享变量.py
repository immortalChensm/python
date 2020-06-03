import threading,time

num = 100

def run(a):
    global num
    for i in range(1000000):
        num = num+a
        num = num-a

if __name__=='__main__':

    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num)