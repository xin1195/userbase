#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/23.
from tornado import gen

from api.controller.baseController import ApiBaseController
from api.model.loginModel import login_user
from api.model.tokenModel import get_token


class ApiTokenController(ApiBaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")
        self.password = self.get_argument("password", "")

    @gen.coroutine
    def get(self, *args, **kwargs):
        flag = yield login_user(self)
        if flag:
            token = yield get_token(self)
            self.change_to_jsonp(token)
        else:
            self.change_to_jsonp("")

    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield login_user(self)
        if flag:
            token = yield get_token(self)
            self.change_to_jsonp(token)
        else:
            self.change_to_jsonp("")
