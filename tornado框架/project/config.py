import os
BASE_DIR = os.path.dirname(__file__)
options = {
    "port":9000
}

settings = {
    "debug":False,
    '''
    此参数为True表示调试环境下使用
    1、会自动重启，代码编辑后保存触发重启 可以用autorealod=True替换
    2、取消缓存 编译的模板 可以用compiled_template_cache=False
    3、取消缓存 编译的静态文件hash值 可以用static_hash_cache=False
    4、提供追踪功能
    此参数默认为false即生产环境下使用
    '''
    "static_path":os.path.join(BASE_DIR,"statics"),
    "template_path":os.path.join(BASE_DIR,"templates")
}