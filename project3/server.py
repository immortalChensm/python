import tornado.ioloop
import tornado.httpserver
import tornado.web
import config
from Application import Application

if __name__ == '__main__':

    app = Application();
    httpSever = tornado.httpserver.HTTPServer(app)
    httpSever.bind(config.config["port"])
    httpSever.start(1)

    tornado.ioloop.IOLoop.current().start()