import tornado.web
import tornado.ioloop
import tornado.httpserver
import config

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello,laotou")

if __name__=='__main__':
    print(config.options.list)
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])

    httpSever = tornado.httpserver.HTTPServer(app)
    httpSever.bind(config.options["port"])
    httpSever.start()
    tornado.ioloop.IOLoop.current().start()