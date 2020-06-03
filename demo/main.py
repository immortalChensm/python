import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define,options
from common.url_router import include,url_wrapper

class Application(tornado.web.Application):
    def __init__(self):
        handlers = url_wrapper([
            (r'/users/',include('views.users.users_urls'))
        ])

        print(handlers)
        settings = dict(
            debut=True,
            static_path=os.path.join(os.path.dirname(__file__),'/static'),
            template_path=os.path.join(os.path.dirname(__file__),'/template')
        )
        tornado.web.Application.__init__(self,handlers,**settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(8888,xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
