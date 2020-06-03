import threading,time
bar = threading.Barrier(4)
'''

barrier	英[ˈbæriə(r)]
美[ˈbæriɚ]
n.	屏障; 障碍; 栅栏; 分界线;
vt.	把…关入栅栏; 用栅栏围住;

'''
def run():
    print("线程%s--start"%(threading.current_thread().name))
    time.sleep(1)
    bar.wait()

    print("线程%s---end"%(threading.current_thread().name))

if __name__=='__main__':
    for i in range(5):
        threading.Thread(target=run).start()