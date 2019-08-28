
from lib import common
from db import db_handle

def register_interface(username,pwd):
    """注册接口"""
    flag = common.check_user(username)
    if flag:
        return False,'用户已存在'
    else:
        content = {'username':username,'pwd':pwd,'extra':15000,'locked':0}
        db_handle.sava_json(username,content)
        return True,'用户注册成功'

def login_interface(username,pwd):
    # 判断用户是否存在
    flag = common.check_user(username)
    if not flag:
        return False,'用户名不存在',1
    
    # 判断用户是否锁定
    data = db_handle.read_json(username)
    if data['locked']:
        return False,'用户已经锁定，去解锁',2

    # 判断密码
    if pwd == data['pwd']:
        return True,'登录成功',0

    return False,'密码错误',3

def locked_interface(username):
    """输入密码就锁"""
    data = db_handle.read_json(username)
    data['locked'] = 1
    db_handle.sava_json(username,data)