import threading


def run():
    print("我5秒后运行")

t = threading.Timer(5,run)
t.start()
t.join()

print("父线程结束")