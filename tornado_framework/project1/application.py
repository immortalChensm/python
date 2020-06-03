import tornado.web
import views.index as index
import config
import os
class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/student",index.StudentHandler),
            (r"/student2",index.Student2Handler),
            (r"/home",index.HomeHandler),
            (r"/chat",index.ChatHandler),

        ]

        super(Application,self).__init__(handler,**config.settings)