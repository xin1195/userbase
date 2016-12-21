#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
import traceback

from tornado import gen

from setting import logger


@gen.coroutine
def get_department_list(self):
    try:
        department_list = []
        query = {}
        if self.department_name:
            query["department_name"] = self.department_name
        show = {"_id": 0}
        cursor = self.motor_db.sys_department.find(query, show).skip((self.page - 1) * self.num).limit(self.num)
        while (yield cursor.fetch_next):
            department = cursor.next_object()
            department_list.append(department)
        return department_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def get_department_one(self):
    try:
        department_list = []
        query = {"department_id": self.department_id}
        show = {"_id": 0}
        department = yield self.motor_db.sys_department.find_one(query, show)
        department_list.append(department)
        return department_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def create_department(self):
    try:
        department_dict = {
            "department_id": self.department_id,
            "department_name": self.department_name,
        }
        query = {"department_id": self.department_id}
        yield self.motor_db.sys_department.update(query, department_dict, upsert=True)
        return 0, "success", "create ok"
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def update_department(self):
    try:
        company_dict = {}
        for company in self.company_list:
            temp = tuple(eval(company))
            company_dict[temp[0]] = temp[1]
        department_dict = {
            "department_name": self.department_name,
            "parent_id": self.parent_id
        }
        if company_dict:
            department_dict["company"] = company_dict
        query = {"department_id": self.department_id}
        yield self.motor_db.sys_department.update(query, {"$set": department_dict}, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_department_one(self):
    try:
        query = {"department_id": self.department_id}
        yield self.motor_db.sys_department.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_department_list(self):
    try:
        query = {"department_id": {"$in": self.department_id}}
        yield self.motor_db.sys_department.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""
