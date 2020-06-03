import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port",default="8000",type=int,help='要监听的端口号')
tornado.options.define("list",default=[],type=str,help='要保存的列表数据',multiple=True)

"""
tornado框架.options 模块功能：
全局选项变量的定义，存储，转换
tornado框架.options.define()
tornado框架.options.otions
tornado框架.parse_commend_line()
"""

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello,options")

if __name__=='__main__':

    """
    全局选项变量命令的转换，在命令行下启动时传递过来，此方法接受
    并保存在tornado.options模块的options对象作为其成员属性
    """
    tornado.options.parse_command_line()
    print(tornado.options.options.list)
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(tornado.options.options.port)
    httpServer.start()

    tornado.ioloop.IOLoop.current().start()