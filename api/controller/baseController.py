#!/usr/bin/env python3
# _*_coding:utf-8_*_


# 基类
import json
import time
import traceback

import tornado.web

from setting import logger


class ApiBaseController(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(ApiBaseController, self).__init__(application, request, **kwargs)
        self.callback = self.get_argument("callback", "")
        self.start_time = time.time()
        self._from = self.get_argument("from", "")
        self.token = self.get_argument("token", "")
        self.version = self.get_argument("version", "1.0.0")
        self.system = self.get_argument("system", "wallpaper")
        self.page = int(self.get_argument("page", 1))
        self.num = int(self.get_argument("num", 10))

    def data_received(self, chunk):
        pass

    def change_to_jsonp(self, results="", page_info_dict={}):
        """
        将返回的结果根据是否存在 callback 参数转换成jsonp格式，主要是提供给网站使用
        :param page_info_dict:
        :param results:
        :return: 将转换后的结果返回给页面
        """
        return_data = {
            "code": 200,
            "time": time.time() - self.start_time,
            "data": results
        }
        if page_info_dict:
            return_data["page_info"] = page_info_dict
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

    def on_finish(self):
        pass
