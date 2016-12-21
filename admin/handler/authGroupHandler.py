#!/usr/bin/env python3
# coding=utf-8
# Created by shein on 2016/12/19
from tornado import gen

from admin.handler.baseHandler import BaseController


class AuthGroupHandler(BaseController):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render("admin/auth_group.html")
