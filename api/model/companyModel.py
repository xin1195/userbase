#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/25.
import traceback

from tornado import gen

from setting import g_motor_db, logger


@gen.coroutine
def get_company_list(self):
    try:
        company_list = []
        query = {}
        if self.company_name:
            query["company_name"] = self.company_name
        if self.address:
            query["address"] = self.address
        show = {"_id": 0}
        cursor = g_motor_db.sys_company.find(query, show).skip((self.page - 1) * self.num).limit(self.num)
        while (yield cursor.fetch_next):
            company = cursor.next_object()
            company_list.append(company)
        return company_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def get_company_one(self):
    try:
        company_list = []
        query = {"company_id": self.company_id}
        show = {"_id": 0}
        company = yield g_motor_db.sys_company.find_one(query, show)
        company_list.append(company)
        return company_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def create_company(self):
    try:
        query = {"company_id": self.company_id}
        company_dict = {
            "company_id": self.company_id,
            "company_name": self.company_name,
            "address": self.address,
            "tell_phone": self.tell_phone,
            "parent_id": self.parent_id
        }
        yield g_motor_db.sys_company.update(query, company_dict, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def update_company(self):
    try:
        query = {"company_id": self.company_id}
        company_dict = {
            "company_name": self.company_name,
            "address": self.address,
            "tell_phone": self.tell_phone,
            "parent_id": self.parent_id
        }
        yield g_motor_db.sys_company.update(query, {"$set": company_dict}, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_company_one(self):
    try:
        query = {"company_id": self.company_id}
        yield g_motor_db.sys_company.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_company_list(self):
    try:
        query = {"company_id": {"$in": self.company_id}}
        yield g_motor_db.sys_company.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""
