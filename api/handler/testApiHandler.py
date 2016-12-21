#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin
# Time 2016/8/23.
from api.handler.baseApiHandler import ApiBaseHandler
from api.model.testModel import get_test


class ApiTestHandler(ApiBaseHandler):
    def get(self, *args, **kwargs):
        results = get_test()
        self.change_to_jsonp(results)
