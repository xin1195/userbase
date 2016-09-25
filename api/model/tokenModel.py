#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/23.
import hashlib
import time
import traceback

from tornado import gen

from common.commonLib import set_token_to_redis
from setting import logger


@gen.coroutine
def get_token(self):
    try:
        token = hashlib.sha256((self.username + str(time.time())).encode('utf-8')).hexdigest()
        set_token_to_redis(self.username, token)
        return token
    except:
        logger.error(traceback.format_exc())
        return ""

