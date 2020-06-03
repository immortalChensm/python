import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello,tornado framework")

if __name__=='__main__':

    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])
    app.listen(8090)
    tornado.ioloop.IOLoop.current().start()