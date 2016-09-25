#!/usr/bin/env python3
# _*_coding:utf-8_*_
# Created by "LiuXin"
# Time 2016/6/27
import os
import traceback

import geoip2.database
import motor.motor_tornado
import re
import redis
import requests


def get_myip():
    """
    :return: 本机的外网ip
    """
    url = "http://myip.liuhub.com/api/get_ip"
    res = requests.get(url)
    myip = res.text
    if myip:
        return myip
    else:
        myip = "112.74.204.250"
        cmd = "curl ip.cn > ip.txt"
        os.system(cmd)
        file_object = open('ip.txt')
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        temp_ip = re.findall(r'\d+.\d+.\d+.\d+', all_the_text)
        if temp_ip:
            myip = temp_ip[-1]
        return myip


def get_isocode(remote_address):
    """
    根据请求ip过去国家编码
    :param remote_address: ip 地址
    :return: 国家代码 （大写）
    """
    try:
        lib_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'common/GeoIP2-Country.mmdb')
        reader = geoip2.database.Reader(lib_path)
        response = reader.country(remote_address.strip())
        iso_code = response.country.iso_code
        reader.close()
    except Exception as ex:
        iso_code = 'US'
    return iso_code


def get_mongodb_db(flag):
    """
    :param flag: 数据选择 debug=True 测试库， False 线上库
    :return: database 数据库， g_motor_client 基于motor的连接 ，g_py_client 基于 pymongo 的连接
    """
    try:
        if flag == "CN":
            # 国内库
            mongodb_path = 'mongodb://127.0.0.1:27017'
            g_motor_db = motor.motor_tornado.MotorClient(mongodb_path).userbase
            g_redis_db = redis.StrictRedis(host='127.0.0.1', port=6379, password="", db=0)
            return "国内 112.74.204.250 userbase", g_motor_db, g_redis_db
        else:
            # 国外库
            mongodb_path = 'mongodb://127.0.0.1:27017'
            g_motor_db = motor.motor_tornado.MotorClient(mongodb_path).userbase
            g_redis_db = redis.StrictRedis(host='127.0.0.1', port=6379, password="", db=0)
            return "国外 112.74.204.250 userbase", g_motor_db, g_redis_db
    except:
        traceback.format_exc()
        return 0


def get_mongodb():
    return get_mongodb_db(get_isocode(get_myip()))
