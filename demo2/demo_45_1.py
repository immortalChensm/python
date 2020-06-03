'''
这是一个自定义的模块
里面定义了3个函数提供使用

'''
#此文件在运行的时候，先获取当前文件的名称，是自己执行时就为__main__，在其它地方运行的时候
#为文件名称即demo_45_1
if __name__ == '__main__':
    print("这是一个模块文件")
else:
    def sayHello():
        print("hello")


    def sayHi():
        print("hi")


    def sayNice():
        print("nice")
