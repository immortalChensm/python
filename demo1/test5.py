import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
tornado.options.define("port",default="9000",type=int,help='端口号配置')
tornado.options.define("list",default=[],type=str,multiple=True)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello,laobiao")

if __name__=='__main__':
    """
    从配置文件里转换其选项配置变量，并将它作为tornado.options.options对象的成员
    tornado框架.options是模块
    tornado框架.options.optons是对象
    
    """
    tornado.options.options.logging = None
    tornado.options.parse_config_file("config")

    print(tornado.options.options.list)
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])

    httpSever = tornado.httpserver.HTTPServer(app)
    httpSever.bind(tornado.options.options.port)
    httpSever.start(1)

    tornado.ioloop.IOLoop.current().start()