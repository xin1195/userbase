#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/29.
from tornado import gen

from api.controller.baseController import ApiBaseController
from api.model.userAuthModel import get_user_auth
from common.decoratorLib import auth_token


class ApiUserAuthController(ApiBaseController):
    """
    获取用户权限
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")
        self.url_node_id = self.get_argument("url_node_id", "")

    @gen.coroutine
    def get(self, *args, **kwargs):
        user_auth_dict = yield get_user_auth(self)
        if self.url_node_id in user_auth_dict:
            self.change_to_jsonp(1)
        else:
            self.change_to_jsonp(0)

    @gen.coroutine
    def post(self, *args, **kwargs):
        user_auth_dict = yield get_user_auth(self)
        if self.url_node_id in user_auth_dict:
            self.change_to_jsonp(1)
        else:
            self.change_to_jsonp(0)
