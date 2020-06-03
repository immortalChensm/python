import tornado.web
import tornado.ioloop
import tornado.httpserver

class indexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello,word")
if __name__=='__main__':

    app = tornado.web.Application([
        (r"/",indexHandler)
    ])

    httpServer = tornado.httpserver.HTTPServer(app)
    #httpServer.listen(8090,'0.0.0.0')

    httpServer.bind(8091,'0.0.0.0')
    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()