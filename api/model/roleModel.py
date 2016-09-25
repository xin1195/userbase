#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
import traceback

from tornado import gen

from setting import g_motor_db, logger


@gen.coroutine
def get_role_list(self):
    try:
        role_list = []
        query = {}
        if self.role_name:
            query["role_name"] = self.role_name
        show = {"_id": 0}
        cursor = g_motor_db.sys_role.find(query, show).skip((self.page - 1) * self.num).limit(self.num)
        while (yield cursor.fetch_next):
            role = cursor.next_object()
            role_list.append(role)
        return role_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def get_role_one(self):
    try:
        role_list = []
        query = {"role_id": self.role_id}
        show = {"_id": 0}
        role = yield g_motor_db.sys_role.find_one(query, show)
        role_list.append(role)
        return role_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def create_role(self):
    try:
        system_dict = {}
        for system in self.system_list:
            temp = tuple(eval(system))
            system_dict[temp[0]] = temp[1]
        node_dict = {}
        for node in self.node_list:
            temp = tuple(eval(node))
            node_dict[temp[0]] = temp[1]
        query = {"role_id": self.role_id}
        role_dict = {
            "role_id": self.role_id,
            "role_name": self.role_name,
        }
        if system_dict:
            role_dict["system"] = system_dict
        if node_dict:
            role_dict["node"] = node_dict
        yield g_motor_db.sys_role.update(query, role_dict, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def update_role(self):
    try:
        system_dict = {}
        for system in self.system_list:
            temp = tuple(eval(system))
            system_dict[temp[0]] = temp[1]
        node_dict = {}
        for node in self.node_list:
            temp = tuple(eval(node))
            node_dict[temp[0]] = temp[1]
        query = {"role_id": self.role_id}
        role_dict = {
            "role_name": self.role_name,
        }
        if system_dict:
            role_dict["system"] = system_dict
        if node_dict:
            role_dict["node"] = node_dict
        yield g_motor_db.sys_role.update(query, {"$set": role_dict}, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_role_one(self):
    try:
        query = {"role_id": self.role_id}
        yield g_motor_db.sys_role.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_role_list(self):
    try:
        query = {"role_id": {"$in": self.role_id}}
        yield g_motor_db.sys_role.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""
