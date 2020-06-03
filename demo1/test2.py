import tornado.web
'''
tornado框架 web模块 负责创建web服务
'''
import tornado.ioloop
'''
tornado框架 IOloop IO轮询模块
'''
import tornado.httpserver
'''
tornado框架 http服务器模块
'''

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("http server running")

if __name__ == '__main__':

    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])

    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(8000)

    """
    这里启动了IOloop.current()实例，它会一直访问linux epoll
    linux epoll 管理socket的读写，有客户端连接时，创建socket
    创建的socket可以进行IO读取操作
    
    同时tornado.web会收到socket的数据
    然后加载路由映射表
    当请求地址是根路径的时候/找到IndexHanlder类
    并执行get方法，返回一个字符串
    """
    tornado.ioloop.IOLoop.current().start()