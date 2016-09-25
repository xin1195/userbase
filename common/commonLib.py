#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/23.
import json

from setting import g_redis_db, g_redis_time_5m, g_redis_time_30m, g_redis_on


def set_token_to_redis(username, token):
    """
    将token数据存入redis缓存数据库
    :param username: 用户名
    :param token: token
    :return:
    """
    if g_redis_on:
        g_redis_db.set(token, json.dumps(username), g_redis_time_30m)


def get_token_to_redis(token):
    """
    将token数据从redis缓存数据库取出
    :param token: token
    :return:
    """
    username = g_redis_db.get(token)
    return username


def set_node_to_redis(username, node_dict):
    """
    将 node 数据存入redis缓存数据库
    :param username: 用户名
    :param node_dict: node_dict
    :return:
    """
    if g_redis_on:
        g_redis_db.set(username, json.dumps(node_dict), g_redis_time_30m)


def get_node_to_redis(username):
    """
    将 node 数据从redis缓存数据库取出
    :param username: username
    :return:
    """
    node_dict = g_redis_db.get(username)
    return node_dict


def get_redis_by_url(self):
    """
    从redis缓存数据库获取数据 根据url
    :param self:
    :return:
    """
    redis_data = g_redis_db.get(self.request.uri)
    if redis_data:
        data_dict = json.loads(redis_data.decode())
    else:
        data_dict = {}
    return data_dict


def set_redis_by_url(self, data_dict):
    """
    将数据存入redis缓存服务器
    :param self:
    :param data_dict:
    :return:
    """
    if g_redis_on and data_dict:
        g_redis_db.set(self.request.uri, json.dumps(data_dict), g_redis_time_5m)
