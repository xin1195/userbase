#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
from tornado import gen

from api.controller.baseController import ApiBaseController
from api.model.companyModel import get_company_one, get_company_list, create_company, update_company, del_company_list, del_company_one
from common.decoratorLib import auth_token


class ApiCompanyRetrieveController(ApiBaseController):
    """
    获取公司类列表
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.company_id = self.get_argument("company_id", "")
        self.company_name = self.get_argument("company_name", "")
        self.address = self.get_argument("address", "")

    @auth_token
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.company_id:
            company_list = yield get_company_one(self)
        else:
            company_list = yield get_company_list(self)
        self.change_to_jsonp(company_list)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.company_id:
            company_list = yield get_company_one(self)
        else:
            company_list = yield get_company_list(self)
        self.change_to_jsonp(company_list)


class ApiCompanyCreateController(ApiBaseController):
    """
    创建一个公司对象
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.company_id = self.get_argument("company_id", "")
        self.company_name = self.get_argument("company_name", "")
        self.address = self.get_argument("address", "")
        self.tell_phone = self.get_argument("tell_phone", "")
        self.parent_id = self.get_argument("parent_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield create_company(self)
        self.change_to_jsonp(flag)


class ApiCompanyUpdateController(ApiBaseController):
    """
    修改一个公司对象
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.company_id = self.get_argument("company_id", "")
        self.company_name = self.get_argument("company_name", "")
        self.address = self.get_argument("address", "")
        self.tell_phone = self.get_argument("tell_phone", "")
        self.parent_id = self.get_argument("parent_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield update_company(self)
        self.change_to_jsonp(flag)


class ApiCompanyDeleteController(ApiBaseController):
    """
    删除一个公司对象
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.company_id = self.get_argument("company_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if type(self.company_id) == list:
            flag = yield del_company_list(self)
            self.change_to_jsonp(flag)
        else:
            flag = yield del_company_one(self)
            self.change_to_jsonp(flag)
