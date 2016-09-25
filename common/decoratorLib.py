#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/24.
from common.commonLib import get_token_to_redis
from setting import g_msg_token


def auth_token(func):
    """
    token验证装饰器
    :param func:
    :return:
    """
    def inner(self, *args, **kwargs):
        username = get_token_to_redis(self.token)
        if username:
            return func(self, *args, **kwargs)
        else:
            self.change_to_jsonp(g_msg_token)
    return inner
