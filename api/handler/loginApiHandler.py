#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/23.
from tornado import gen

from api.handler.baseApiHandler import ApiBaseHandler
from api.model.loginModel import login_user


class ApiLoginHandler(ApiBaseHandler):
    """
    登录接口
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")
        self.password = self.get_argument("password", "")

    @gen.coroutine
    def post(self, *args, **kwargs):
        user = yield login_user(self)
        self.change_to_jsonp(user)

