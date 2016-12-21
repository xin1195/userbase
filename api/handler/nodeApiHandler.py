#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.

from tornado import gen

from api.handler.baseApiHandler import ApiBaseHandler
from api.model.nodeModel import get_node_list, del_node_list, del_node_one, create_node, update_node
from api.model.nodeModel import get_node_one
from common.decoratorLib import auth_token


class ApiNodeRetrieveHandler(ApiBaseHandler):
    """
    获取公司类列表
    """
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.node_id = self.get_argument("node_id", "")
        self.node_name = self.get_argument("node_name", "")
        self.system_id = self.get_argument("system_id", "")

    @auth_token
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.node_id:
            node_list = yield get_node_one(self)
        else:
            node_list = yield get_node_list(self)
        self.change_to_jsonp(node_list)

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.node_id:
            node_list = yield get_node_one(self)
        else:
            node_list = yield get_node_list(self)
        self.change_to_jsonp(node_list)


class ApiNodeCreateHandler(ApiBaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.node_id = self.get_argument("node_id", "")
        self.node_name = self.get_argument("node_name", "")
        self.system_id = self.get_argument("system_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield create_node(self)
        self.change_to_jsonp(flag)


class ApiNodeUpdateHandler(ApiBaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.node_id = self.get_argument("node_id", "")
        self.node_name = self.get_argument("node_name", "")
        self.system_id = self.get_argument("system_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        flag = yield update_node(self)
        self.change_to_jsonp(flag)


class ApiNodeDeleteHandler(ApiBaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.node_id = self.get_argument("node_id", "")

    @auth_token
    @gen.coroutine
    def post(self, *args, **kwargs):
        if type(self.node_id) == list:
            flag = yield del_node_list(self)
            self.change_to_jsonp(flag)
        else:
            flag = yield del_node_one(self)
            self.change_to_jsonp(flag)
