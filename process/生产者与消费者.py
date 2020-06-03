import threading,queue,os,time,random

def product(id,q):
    while True:
        num = random.randint(0,10000)
        q.put(num)
        print("生产者%d生产了数据%d"%(id,num))
        time.sleep(3)
    q.task_done()

def consumer(id,q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d消费了%d数据"%(id,item))
    q.task_done()

if __name__=='__main__':
    #消息列队
    q = queue.Queue()
    #生产者
    for i in range(4):
        threading.Thread(target=product,args=(i,q)).start()
    #消费者
    for i in range(3):
        threading.Thread(target=consumer, args=(i,q)).start()
