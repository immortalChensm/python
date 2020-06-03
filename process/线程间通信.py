import threading
import time
def fund():
    event = threading.Event()
    def run():
        for i in range(5):
            #事件阻塞  等待事件触发后运行
            event.wait()
            event.clear()
            print("%d"%i)

    threading.Thread(target=run).start()
    return event

e = fund()

for i in range(5):
    time.sleep(2)
    e.set()#线程事件触发