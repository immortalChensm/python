import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

tornado.options.options.define(name="port",default=8090,type=str)
tornado.options.options.define(name="address",default="0.0.0.0",type=str)
tornado.options.options.define(name="list",default=[],type=str)
class indexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hi,tornado")
if __name__=='__main__':
    tornado.options.parse_command_line()
    print(tornado.options.options.list)
    app = tornado.web.Application([
        (r"/",indexHandler)
    ])

    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.bind(port=tornado.options.options.port,address=tornado.options.options.address)
    httpserver.start(1)

    tornado.ioloop.IOLoop.current().start()