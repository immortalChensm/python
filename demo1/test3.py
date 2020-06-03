import tornado.web
import tornado.ioloop
import tornado.httpserver
import time

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello,world"+str(time.strftime('%Y-%m-%d',time.localtime(time.time()))))



if __name__=='__main__':
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])
    """
    手动创建一个httpserver
    并绑定端口9000
    同时启动一个进程数
    """
    httpSever = tornado.httpserver.HTTPServer(app)
    httpSever.bind(9000)
    """
    num_process=1默认启动一个进程
    """
    httpSever.start(1)

    """
    此程序有3个问题
    1、多个进程共用一个端口
    2、一个命令启动多个进程，无法实现一个进程监听一个命令
    3、子进程是复制父进程
    """
    tornado.ioloop.IOLoop.current().start()