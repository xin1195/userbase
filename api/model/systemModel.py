#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
import traceback

from tornado import gen

from setting import g_motor_db, logger


@gen.coroutine
def get_system_list(self):
    try:
        system_list = []
        query = {}
        if self.system_name:
            query["system_name"] = self.system_name
        show = {"_id": 0}
        cursor = g_motor_db.sys_system.find(query, show).skip((self.page - 1) * self.num).limit(self.num)
        while (yield cursor.fetch_next):
            system = cursor.next_object()
            system_list.append(system)
        return system_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def get_system_one(self):
    try:
        system_list = []
        query = {"system_id": self.system_id}
        show = {"_id": 0}
        system = yield g_motor_db.sys_system.find_one(query, show)
        system_list.append(system)
        return system_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def create_system(self):
    try:
        company_dict = {}
        department_dict = {}
        for company in self.company_list:
            temp = tuple(eval(company))
            company_dict[temp[0]] = temp[1]
        for department in self.department_list:
            temp = tuple(eval(department))
            department_dict[temp[0]] = temp[1]
        system_dict = {
            "system_id": self.system_id,
            "system_name": self.system_name,
        }
        if company_dict:
            system_dict["company"] = company_dict
        if department_dict:
            system_dict["department"] = department_dict
        query = {"system_id": self.system_id}
        yield g_motor_db.sys_system.update(query, system_dict, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def update_system(self):
    try:
        company_dict = {}
        department_dict = {}
        for company in self.company_list:
            temp = tuple(eval(company))
            company_dict[temp[0]] = temp[1]
        for department in self.department_list:
            temp = tuple(eval(department))
            department_dict[temp[0]] = temp[1]
        system_dict = {
            "system_id": self.system_id,
            "system_name": self.system_name,
        }
        if company_dict:
            system_dict["company"] = company_dict
        if department_dict:
            system_dict["department"] = department_dict
        query = {"system_id": self.system_id}
        yield g_motor_db.sys_system.update(query, {"$set": system_dict}, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_system_one(self):
    try:
        query = {"system_id": self.system_id}
        yield g_motor_db.sys_system.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_system_list(self):
    try:
        query = {"system_id": {"$in": self.system_id}}
        yield g_motor_db.sys_system.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""
