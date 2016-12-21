#!/usr/bin/env python3
# _*_coding:utf-8_*_


import tornado.web

from setting import g_motor_db, g_redis_db


class BaseController(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseController, self).__init__(application, request, **kwargs)
        self.motor_db = g_motor_db
        self.redis_db = g_redis_db

    def data_received(self, chunk):
        pass

    def on_finish(self):
        pass
