

1、先获取日志器
logger = logging.getLogger()
2、设置日志器的日志级别
logger.setLevel(logging.DEBUG,INFO,NOTSET)
3、得到一个日志文件句柄
log_file_handler = logging.FileHanlder(filename)
4、设置日志文件等级
log_file_handler.setLevel
5、设置日志文件的格式化
loggin.Formatter
log_file_handler.SetFormatter
6、添加日志句柄

7、运行日志方法
loggin.info
loggin.debug
logging.error
loggin.warning
logging.cirtical