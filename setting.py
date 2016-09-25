#!/usr/bin/env python3
# _*_coding:utf-8_*_

# 设置文件配置
from conf.loggerLib import get_logger
from conf.settingLib import get_mongodb

settings = dict(
    # template_path=os.path.join(os.path.dirname(__file__), "templates"),
    # static_path=os.path.join(os.path.dirname(__file__), "static"),
    # cookie_secret="bZJc2sWbQLKosdcdGkHn/VytrsDghDuyhfksdfsSDSsdfJ5/xJ89E=",
    # login_url="/login",
    # xsrf_cookies=True,
    debug=False,
)

# 日志模块
logger = get_logger(strFileName="userBase_api.log",
                    debug=20,
                    showStreamLog=True,
                    saveLogPath=None)

# 获取数据库连接
if get_mongodb():
    database, g_motor_db, g_redis_db = get_mongodb()
    logger.warning("(%s)数据库连接成功" % database)
else:
    logger.error("数据库连接失败")


# 是否把数据写入redis： False 表示不写入redis， True表示写入redis
g_redis_on = True

# redis 数据保存时间
g_redis_time_5m = 5 * 60
g_redis_time_10m = 10 * 60
g_redis_time_30m = 30 * 60
g_redis_time_1h = 1 * 60 * 60


# 语言转成国家
g_dict_app_country = {
    # 中国
    "zh_hant_hk": "CN", "zh_hans_sg": "CN", "zh_hans_hk": "CN", "zh_hans": "CN", "zh": "CN", "zh_hans_cn": "CN", "zh_hant": "CN",
    "zh_hant_tw": "CN", "zh_hant_mo": "CN", "zh_hans_mo": "CN",
    "zh-hant_hk": "CN", "zh-hans-sg": "CN", "zh-hans-hk": "CN", "zh-hans": "CN", "zh-hans-cn": "CN", "zh-hant": "CN",
    "zh-hant-tw": "CN", "zh-hant-mo": "CN", "zh-hans-mo": "CN",
    # 美国
    "us": "US",
    "en": "US",
    # 阿拉伯
    'ar_ye': "SA", 'ar_eg': "SA", 'ar_sa': "SA", 'ar_sd': "SA", 'ar_ly': "SA", 'ar_om': "SA", 'ar_ma': "SA", 'ar_tn': "SA", 'ar_jo': "SA",
    'ar_kw': "SA", 'ar_qa': "SA", 'ar_lb': "SA", 'ar_iq': "SA", 'ar_bh': "SA", 'ar': "SA", 'ar_ae': "SA", 'ar_dz': "SA", 'ar_sy': "SA",
    'ar-ye': "SA", 'ar-eg': "SA", 'ar-sa': "SA", 'ar-sd': "SA", 'ar-ly': "SA", 'ar-om': "SA", 'ar-ma': "SA", 'ar-tn': "SA", 'ar-jo': "SA",
    'ar-kw': "SA", 'ar-qa': "SA", 'ar-lb': "SA", 'ar-iq': "SA", 'ar-bh': "SA", 'ar-ae': "SA", 'ar-dz': "SA", 'ar-sy': "SA",
}

# 图片下载地址 前缀
image_download_path = "http://cdn.dl.pic.apiwallpaper.com/"

# 提示语
g_msg_token = "token 错误或过期，请重新获取token, token有效时间为1800s."


