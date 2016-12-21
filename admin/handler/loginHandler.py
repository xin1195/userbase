#!/usr/bin/env python3
# coding=utf-8
# Created by shein on 2016/12/15
from tornado import gen

from admin.handler.baseHandler import BaseController
from admin.model.loginModel import login


class LoginHandler(BaseController):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.username = self.get_argument("username", "")
        self.password = self.get_argument("password", "")

    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render("admin/login.html")

    @gen.coroutine
    def post(self, *args, **kwargs):
        user = yield login(self)
        self.render("admin/login", user=user)
