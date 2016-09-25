#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
from tornado import gen

from api.controller.baseController import ApiBaseController
from api.model.departmentModel import get_department_list, del_department_list, del_department_one, update_department, create_department
from api.model.departmentModel import get_department_one
from common.decoratorLib import auth_token


class ApiDepartmentRetrieveController(ApiBaseController):
    """
    获取公司类列表
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.department_id = self.get_argument("department_id", "")
        self.department_name = self.get_argument("department_name", "")

    @auth_token
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.department_id:
            department_list = yield get_department_one(self)
        else:
            department_list = yield get_department_list(self)
        self.change_to_jsonp(department_list)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.department_id:
            department_list = yield get_department_one(self)
        else:
            department_list = yield get_department_list(self)
        self.change_to_jsonp(department_list)


class ApiDepartmentCreateController(ApiBaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.department_id = self.get_argument("department_id", "")
        self.department_name = self.get_argument("department_name", "")
        self.company_list = self.get_arguments("company", strip=True)
        self.parent_id = self.get_argument("parent_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield create_department(self)
        self.change_to_jsonp(flag)


class ApiDepartmentUpdateController(ApiBaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.department_id = self.get_argument("department_id", "")
        self.department_name = self.get_argument("department_name", "")
        self.company_list = self.get_arguments("company", strip=True)
        self.parent_id = self.get_argument("parent_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield update_department(self)
        self.change_to_jsonp(flag)


class ApiDepartmentDeleteController(ApiBaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.department_id = self.get_argument("department_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if type(self.department_id) == list:
            flag = yield del_department_list(self)
            self.change_to_jsonp(flag)
        else:
            flag = yield del_department_one(self)
            self.change_to_jsonp(flag)
