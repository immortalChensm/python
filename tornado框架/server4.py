import tornado.web
import tornado.ioloop
import tornado.httpserver
import config
class indexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hi,tornado")
if __name__=='__main__':

    print(config.options['list'])
    app = tornado.web.Application([
        (r"/",indexHandler)
    ])

    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.bind(port=config.options['port'],address=config.options['address'])
    httpserver.start(1)

    tornado.ioloop.IOLoop.current().start()