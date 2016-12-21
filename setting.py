#!/usr/bin/env python3
# _*_coding:utf-8_*_

# 设置文件配置
import os

import motor
import redis

from common.loggerLib import get_logger

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="bZJc2sWbQLKosdcdGkHn/VytrsDghDuyhfksdfsSDSsdfJ5/xJ89E=",
    login_url="/login",
    # xsrf_cookies=True,
    debug=True,
)

# 日志模块
logger = get_logger(strFileName="userBase.log",
                    debug=20,
                    showStreamLog=True,
                    saveLogPath=None)

# 获取数据库连接
try:
    g_motor_db = motor.motor_tornado.MotorClient("mongodb://112.74.204.250:27017").userbase
    g_redis_db = redis.StrictRedis(host='112.74.204.250', port=6379, password="", db=0)
finally:
    logger.info("g_motor_db: %s" % g_motor_db)
    logger.info("g_redis_db: %s" % g_redis_db)

# 是否把数据写入redis： False 表示不写入redis， True表示写入redis
g_redis_on = True

# redis 数据保存时间
g_redis_time_5m = 5 * 60
g_redis_time_10m = 10 * 60
g_redis_time_30m = 30 * 60
g_redis_time_1h = 1 * 60 * 60

# 提示语
g_msg_token = "token 错误或过期，请重新获取token, token有效时间为1800s."

# 公司列表
g_company_dict = {
    "NjLT": "南京领添信息技术有限公司",
    "SzKS": "深圳库尚信息技术有限公司",
    "GzLT": "广州领添分公司",
}
