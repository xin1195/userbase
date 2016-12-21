#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.

from tornado import gen

from api.handler.baseApiHandler import ApiBaseHandler
from api.model.systemModel import get_system_list, del_system_list, del_system_one, create_system
from api.model.systemModel import get_system_one
from api.model.userModel import update_user
from common.decoratorLib import auth_token


class ApiSystemRetrieveHandler(ApiBaseHandler):
    """
    获取公司类列表
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.system_id = self.get_argument("system_id", "")
        self.system_name = self.get_argument("system_name", "")

    @auth_token
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.system_id:
            system_list = yield get_system_one(self)
        else:
            system_list = yield get_system_list(self)
        self.change_to_jsonp(system_list)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.system_id:
            system_list = yield get_system_one(self)
        else:
            system_list = yield get_system_list(self)
        self.change_to_jsonp(system_list)


class ApiSystemCreateHandler(ApiBaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.system_id = self.get_argument("system_id", "")
        self.system_name = self.get_argument("system_name", "")
        self.department_list = self.get_arguments("department", strip=True)
        self.company_list = self.get_arguments("company", strip=True)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield create_system(self)
        self.change_to_jsonp(flag)


class ApiSystemUpdateHandler(ApiBaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.system_id = self.get_argument("system_id", "")
        self.system_name = self.get_argument("system_name", "")
        self.department_list = self.get_arguments("department", strip=True)
        self.company_list = self.get_arguments("company", strip=True)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield update_user(self)
        self.change_to_jsonp(flag)


class ApiSystemDeleteHandler(ApiBaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.system_id = self.get_argument("system_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if type(self.system_id) == list:
            flag = yield del_system_list(self)
            self.change_to_jsonp(flag)
        else:
            flag = yield del_system_one(self)
            self.change_to_jsonp(flag)
