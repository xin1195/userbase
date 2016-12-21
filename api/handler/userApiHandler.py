#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin
# Time 2016/8/23.
from tornado import gen

from api.handler.baseApiHandler import ApiBaseHandler
from api.model.userModel import get_user_list, get_user_one, del_user_one, create_user, update_user, del_user_list
from common.decoratorLib import auth_token


class ApiUserRetrieveHandler(ApiBaseHandler):
    """
    获取单个用户类
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")

    @auth_token
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.username:
            user_list = yield get_user_one(self)
        else:
            user_list = yield get_user_list(self)
        self.change_to_jsonp(user_list)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.username:
            user_list = yield get_user_one(self)
        else:
            user_list = yield get_user_list(self)
        self.change_to_jsonp(user_list)


class ApiUserCreateHandler(ApiBaseHandler):
    """
    新增一个用户类
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")
        self.password = self.get_argument("password", "")
        self.tell_phone = self.get_argument("tell_phone", "")
        self.user_real_name = self.get_argument("user_real_name", "")
        self.email = self.get_argument("email", "")
        self.company_list = self.get_arguments("company", strip=True)
        self.department_list = self.get_arguments("department", strip=True)
        self.system_list = self.get_arguments("system", strip=True)
        self.role_list = self.get_arguments("role", strip=True)
        self.position = self.get_argument("position", "")
        self.sex = self.get_argument("sex", "")
        self.age = self.get_argument("age", "")
        self.address = self.get_argument("address", "")
        self.entry_time = self.get_argument("entry_time", "")
        self.regular_time = self.get_argument("regular_time", "")
        self.quit_time = self.get_argument("quit_time", "")
        self.status = self.get_argument("status", "")
        self.review = self.get_argument("review", "")
        self.emergency_contact_name = self.get_argument("emergency_contact_name", "")
        self.emergency_contact_tell_phone = self.get_argument("emergency_contact_tell_phone", "")
        self.emergency_contact_address = self.get_argument("emergency_contact_address", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield create_user(self)
        self.change_to_jsonp(flag)


class ApiUserUpdateHandler(ApiBaseHandler):
    """
    修改一个用户类
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")
        self.password = self.get_argument("password", "")
        self.tell_phone = self.get_argument("tell_phone", "")
        self.user_real_name = self.get_argument("user_real_name", "")
        self.email = self.get_argument("email", "")
        self.company_list = self.get_arguments("company", strip=True)
        self.department_list = self.get_arguments("department", strip=True)
        self.system_list = self.get_arguments("system", strip=True)
        self.role_list = self.get_arguments("role", strip=True)
        self.position = self.get_argument("position", "")
        self.sex = self.get_argument("sex", "")
        self.age = self.get_argument("age", "")
        self.address = self.get_argument("address", "")
        self.entry_time = self.get_argument("entry_time", "")
        self.regular_time = self.get_argument("regular_time", "")
        self.quit_time = self.get_argument("quit_time", "")
        self.status = self.get_argument("status", "")
        self.review = self.get_argument("review", "")
        self.emergency_contact_name = self.get_argument("emergency_contact_name", "")
        self.emergency_contact_tell_phone = self.get_argument("emergency_contact_tell_phone", "")
        self.emergency_contact_address = self.get_argument("emergency_contact_address", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield update_user(self)
        self.change_to_jsonp(flag)


class ApiUserDeleteHandler(ApiBaseHandler):
    """
    删除一个用户类
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if type(self.username) == list:
            flag = yield del_user_list(self)
            self.change_to_jsonp(flag)
        else:
            flag = yield del_user_one(self)
            self.change_to_jsonp(flag)

