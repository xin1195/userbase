#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
from tornado import gen

from api.handler.baseApiHandler import ApiBaseHandler
from api.model.departmentModel import get_department_list, create_department
from api.model.departmentModel import get_department_one
from common.decoratorLib import auth_token


class ApiDepartmentHandler(ApiBaseHandler):
    """
    部门类管理
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.department_id = self.get_argument("department_id", "")
        self.department_name = self.get_argument("department_name", "")
        self.department_desc = self.get_argument("department_desc", "")
        self.company_name = self.get_arguments("company_name")
        self.action = self.get_argument("action", "")

    @auth_token
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.action == "search":
            department_list = yield get_department_one(self)
        else:
            department_list = yield get_department_list(self)
        self.change_to_jsonp(department_list)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.action == "create":
            yield create_department(self)
        elif self.action == "update":
            pass
        elif self.action == "disable":
            pass
        else:
            pass
