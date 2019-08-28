import os
import logging.config
#####
# 功能字典 #
#####
# 功能字典
FUNC_MSG = {
    '0':'注销',
    '1':'登录',
    '2':'注册',
    '3':'查看余额',
    '4':'转账',
    '5':'还款',
    '6':'取款',
    '7':'查看流水',
    '8':'购物',
    '9':'购物车',
    'q':'退出'
}




######################
# db/log文件夹路径名 #
######################
ATM_PATH = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ATM_PATH,'db')
LOG_PATH = os.path.join(ATM_PATH,'log')
GOODS_INFO_PATH = os.path.join(DB_PATH,'goods_info.xlsx')

###############
# logging配置 #
###############
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getLogger()指定的名字；lineno为调用日志输出函数的语句所在的代码行
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# ********
logfile_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logfile_dir = os.path.join(logfile_dir, 'log')
logfile_name = 'log.log'
# *****

if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

logfile_path = os.path.join(logfile_dir, logfile_name)
# print('logfile_path:',logfile_path)
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},  # filter可以不定义
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M  (*****)
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态

    return logger

if __name__ == '__main__':
    load_my_logging_cfg()