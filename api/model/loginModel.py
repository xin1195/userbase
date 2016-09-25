#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/23.
import hashlib
import traceback

from tornado import gen

from setting import g_motor_db, logger


@gen.coroutine
def login_user(self):
    """
    通过username和password获得user
    :param self:
    :return:
    """
    try:
        salt = hashlib.md5(self.username.encode('utf-8')).hexdigest()
        hash_password = hashlib.sha256((self.password + salt).encode('utf-8')).hexdigest()
        query = {"username": self.username, "password": hash_password, "system." + self.system: {"$exists": 1}}
        show = {"_id": 0, "username": 1}
        user = yield g_motor_db.sys_user.find_one(query, show)
        if user:
            return 1
        else:
            return 0
    except:
        logger.error(traceback.format_exc())
        return 0
