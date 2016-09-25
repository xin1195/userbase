#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin
# Time 2016/8/23.
from api.controller.baseController import ApiBaseController
from api.model.testModel import get_test


class ApiTestController(ApiBaseController):
    def get(self, *args, **kwargs):
        results = get_test()
        self.change_to_jsonp(results)
