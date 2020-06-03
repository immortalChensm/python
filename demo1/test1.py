import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello,tornado框架")
if __name__ == '__main__':

    app = tornado.web.Application([
        (r'/',IndexHandler)
    ])

    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()