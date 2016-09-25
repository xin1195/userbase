#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.

from tornado import gen

from api.controller.baseController import ApiBaseController
from api.model.roleModel import get_role_list, del_role_one, del_role_list, create_role, update_role
from api.model.roleModel import get_role_one
from common.decoratorLib import auth_token


class ApiRoleRetrieveController(ApiBaseController):
    """
    获取公司类列表
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.role_id = self.get_argument("role_id", "")
        self.role_name = self.get_argument("role_name", "")

    @auth_token
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.role_id:
            role_list = yield get_role_one(self)
        else:
            role_list = yield get_role_list(self)
        self.change_to_jsonp(role_list)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.role_id:
            role_list = yield get_role_one(self)
        else:
            role_list = yield get_role_list(self)
        self.change_to_jsonp(role_list)


class ApiRoleCreateController(ApiBaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.role_id = self.get_argument("role_id", "")
        self.role_name = self.get_argument("role_name", "")
        self.system_list = self.get_arguments("system", strip=True)
        self.node_list = self.get_arguments("node", strip=True)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield create_role(self)
        self.change_to_jsonp(flag)


class ApiRoleUpdateController(ApiBaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.role_id = self.get_argument("role_id", "")
        self.role_name = self.get_argument("role_name", "")
        self.system_list = self.get_arguments("system", strip=True)
        self.node_list = self.get_arguments("node", strip=True)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield update_role(self)
        self.change_to_jsonp(flag)


class ApiRoleDeleteController(ApiBaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.role_id = self.get_argument("role_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if type(self.role_id) == list:
            flag = yield del_role_list(self)
            self.change_to_jsonp(flag)
        else:
            flag = yield del_role_one(self)
            self.change_to_jsonp(flag)
