#!/usr/bin/env python3
# _*_coding:utf-8_*_


# 基类
import json
import time
import traceback

import tornado.web

from setting import logger, g_motor_db


class ApiBaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(ApiBaseHandler, self).__init__(application, request, **kwargs)
        self.callback = self.get_argument("callback", "")
        self.start_time = time.time()
        self.token = self.get_argument("token", "")
        self.version = self.get_argument("version", "1.0.0")
        self.mongodb = g_motor_db

    def data_received(self, chunk):
        pass

    def change_to_jsonp(self, info=[], result="success", msg="no_error", code="200", sum_num=""):
        """
        将返回的结果根据是否存在 callback 参数转换成jsonp格式，主要是提供给网站使用
        :param sum_num:
        :param code:
        :param msg:
        :param result:
        :param info:
        :return: 将转换后的结果返回给页面
        """
        return_data = {
            "result": result,
            "msg": msg,
            "code": code,
            "time": time.time() - self.start_time,
            "info": info
        }
        if sum_num:
            return_data["sum"] = sum_num
        if self.callback:
            return_data = str(self.callback) + "(" + json.dumps(return_data) + ")"
        self.write(return_data)
        self.finish()
        return

    def write_error(self, status_code, **kwargs):
        logger.error(traceback.format_exc())
        return_data = {
            "code": 500,
            "time": time.time() - self.start_time,
            "data": "请求出错，请联系管理员"
        }
        self.write(return_data)
        self.finish()
        return

    def on_finish(self):
        pass
