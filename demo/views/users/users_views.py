import tornado.web
import sys
from tornado.escape import json_decode
import logging
from imp import reload
from logging.handlers import TimedRotatingFileHandler
from common.commons import (
    http_response,
)

from conf.base import (
    ERROR_CODES,
)



logFilePath = "log/users/users.log"
logger = logging.getLogger('Users')
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(
    logFilePath,
    when='D',
    interval=1,
    backupCount=30
)
formatter = logging.Formatter('%(asctime)s%(filename)s[line:%(lineno)d]%(levelname)s%(message)s',)
handler.suffix='%Y%m%d'
handler.setFormatter(formatter)
logger.addHandler(handler)


class RegistHandle(tornado.web.RequestHandler):

    def post(self):
        try:
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            code = args['code']
        except:
            logger.info("RegistHandle:request param incorrect")
            http_response(self,ERROR_CODES['1001'],1001)
            return

        logger.debug("RegistHandle:regist successfully")
        http_response(self,ERROR_CODES['0'],0)


