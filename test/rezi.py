
"""
print('this is %s'%('jack'))

print('there are many %s and %d'%('apple',500))

print("%(name)s's age is %(age)d years old"%({'name':'jack','age':200}))
import logging

#logging.basicConfig(level=logging.INFO,format='%(asctime)s--%(name)s--%(levelname)s---%(message)s')
#logger = logging.getLogger(__name__)


#logging.info('start run...')
#logging.debug('start debug...')
#logging.warn('warning ...')
#logging.info('run over')

logging.info('hello')
logging.debug(u'日本人')
logging.info(u'老美')
logging.warning(u'错误了')
logging.error(u'对了')
logging.critical('不暴利')
logging.basicConfig(level=logging.NOTSET)

logging.info('haha')
logging.debug('huhu')
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s--%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')

logging.info('准备输出信息')
logging.debug('准备调度')
logging.error('出错了')
logging.warning('警告了')
logging.critical('啥玩意')
import logging
import os
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))

log_path = os.path.dirname(os.getcwd()+'/logs/')

log_name = log_path+rq+'.log'

logfile = log_name

fh = logging.FileHandler(logfile,mode='w')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s--%(filename)s--[line:%(lineno)d]--%(levelname)s--%(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)

logging.info('这里是info信息')
logging.debug('这里是debug信息')
logging.error('这里是error信息')
logging.warning('这里是warning信息')
logging.critical('这里是critical信息')
"""
import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

def backroll():

    log_frm = '%(asctime)s-%(filename)s[line:%(lineno)s]-%(levelname)s-%(message)s'
    formatter = logging.Formatter(log_frm)
    log_file_hander = TimedRotatingFileHandler(filename='logs/ds_update.log',when='D',interval=1,backupCount=30)
    log_file_hander.setFormatter(formatter)
    logging.basicConfig(level=logging.DEBUG)

    log = logging.getLogger()
    log.addHandler(log_file_hander)
    log_content = 'log test'
    count = 0
    while count<30:
        log.error(log_content)
        time.sleep(20)
        count+=1

    log.removeHandler(log_file_hander)




if __name__ == '__main__':
    backroll()