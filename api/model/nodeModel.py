#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
import traceback

from tornado import gen

from setting import g_motor_db, logger


@gen.coroutine
def get_node_list(self):
    try:
        node_list = []
        query = {}
        if self.node_name:
            query["node_name"] = self.node_name
        if self.system_id:
            query["system_id"] = self.system_id
        show = {"_id": 0}
        cursor = g_motor_db.sys_node.find(query, show).skip((self.page - 1) * self.num).limit(self.num)
        while (yield cursor.fetch_next):
            node = cursor.next_object()
            node_list.append(node)
        return node_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def get_node_one(self):
    try:
        node_list = []
        query = {"node_id": self.node_id}
        show = {"_id": 0}
        node = yield g_motor_db.sys_node.find_one(query, show)
        node_list.append(node)
        return node_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def create_node(self):
    try:
        query = {"node_id": self.node_id}
        node_dict = {
            "node_id": self.node_id,
            "node_name": self.node_name,
            "system_id": self.system_id,
        }
        yield g_motor_db.sys_node.update(query, node_dict, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def update_node(self):
    try:
        query = {"node_id": self.node_id}
        node_dict = {
            "node_name": self.node_name,
            "system_id": self.system_id,
        }
        yield g_motor_db.sys_node.update(query, {"$set": node_dict}, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_node_one(self):
    try:
        query = {"node_id": self.node_id}
        yield g_motor_db.sys_node.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_node_list(self):
    try:
        query = {"node_id": {"$in": self.node_id}}
        yield g_motor_db.sys_node.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""
