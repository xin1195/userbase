#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/23.
from tornado import gen

from api.handler.baseApiHandler import ApiBaseHandler
from api.model.websiteModel import update_auth_key, get_website_list, create_website, update_website, disable_website, search_website


class ApiWebsiteHandler(ApiBaseHandler):
    """
    站点接口
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.website_code = self.get_argument("website_code", "")
        self.website_name = self.get_argument("website_name", "")
        self.website_domain = self.get_argument("website_domain", "")
        self.website_next = self.get_argument("website_next", "")
        self.action = self.get_argument("action", "add")

    @gen.coroutine
    def get(self, *args, **kwargs):
        info = yield get_website_list(self)
        print("info", info)
        self.change_to_jsonp(info=info)

    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.action == "create":
            code, result, msg = yield create_website(self)
            self.change_to_jsonp(code=code, result=result, msg=msg)
        elif self.action == "update":
            code, result, msg = yield update_website(self)
            self.change_to_jsonp(code=code, result=result, msg=msg)
        elif self.action == "disable":
            code, result, msg = yield disable_website(self)
            self.change_to_jsonp(code=code, result=result, msg=msg)
        elif self.action == "search":
            code, result, msg = yield search_website(self)
            self.change_to_jsonp(code=code, result=result, msg=msg)
        else:
            pass


class ApiWebsiteAuthKeyHandler(ApiBaseHandler):
    """
    新增站点authKey接口
    """

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.website_code = self.get_argument("website_code", "")

    @gen.coroutine
    def post(self, *args, **kwargs):
        code, result, msg = yield update_auth_key(self)
        self.change_to_jsonp(code=code, result=result, msg=msg)
