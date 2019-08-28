import os
import hashlib
import logging
import logging.config
from conf import settings

def login_auth(func):
    from core import src
    def wrapper(*args,**kwargs):
        # 判断是否登录
        if not src.user_auth.get('username'):
            src.login()
            res = func(*args,**kwargs)
            return res

        res = func(*args,**kwargs)
        return res

    return wrapper

def load_logging_config(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)

    return logger

def check_user(username):
    """注册接口"""
    db_list = os.listdir(settings.DB_PATH)
    username_filename = os.path.join(settings.DB_PATH,f'{username}.json')
    if os.path.exists(username_filename):
        return True

def input_username_pwd():
    username = input('请输入你的用户名>>>').strip()
    pwd = input('请输入你的密码>>>').strip()

    # 密码加密
    m = hashlib.md5()
    m.update(pwd.encode('utf8'))
    pwd = m.hexdigest()

    return username,pwd

if __name__ == '__main__':
    res = check_user('nick')
    print(res)