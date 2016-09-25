#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin
# Time 2016/8/23.
import hashlib
import traceback
from datetime import datetime

from tornado import gen

from common.checkLib import check_user
from setting import g_motor_db, logger


@gen.coroutine
def get_user_list(self):
    try:
        user_list = []
        query = {}
        show = {"_id": 0, "password": 0}
        cursor = g_motor_db.sys_user.find(query, show).skip((self.page - 1) * self.num).limit(self.num)
        while (yield cursor.fetch_next):
            user = cursor.next_object()
            user_list.append(check_user(user))
        return user_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def get_user_one(self):
    try:
        user_list = []
        query = {"username": self.username}
        show = {"_id": 0, "password": 0}
        user = yield g_motor_db.sys_user.find_one(query, show)
        user_list.append(check_user(user))
        return user_list
    except:
        logger.error(traceback.format_exc())
        return []


@gen.coroutine
def create_user(self):
    try:
        salt = hashlib.md5(self.username.encode('utf-8')).hexdigest()
        hash_password = hashlib.sha256((self.password + salt).encode('utf-8')).hexdigest()
        company_dict = {}
        department_dict = {}
        system_dict = {}
        role_dict = {}
        for company in self.company_list:
            temp = tuple(eval(company))
            company_dict[temp[0]] = temp[1]
        for department in self.department_list:
            temp = tuple(eval(department))
            department_dict[temp[0]] = temp[1]
        for system in self.system_list:
            temp = tuple(eval(system))
            system_dict[temp[0]] = temp[1]
        for role in self.role_list:
            temp = tuple(eval(role))
            role_dict[temp[0]] = temp[1]
        user_dict = {
            "username": self.username,
            "password": hash_password,
            "tell_phone": self.tell_phone,
            "user_real_name": self.user_real_name,
            "email": self.email,
            "position": self.position,
            "sex": self.sex,
            "age": self.age,
            "address": self.address,
            "entry_time": "",
            "regular_time": "",
            "quit_time": "",
            "status": self.status,
            "review": self.review,
            "emergency_contact": {
                "name": self.emergency_contact_name,
                "tell_phone": self.emergency_contact_tell_phone,
                "address": self.emergency_contact_address,
            },
            "add_time": datetime.now(),
            "last_update_time": datetime.now(),
        }

        if self.entry_time:
            user_dict["entry_time"] = datetime.strptime(self.entry_time + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
        if self.regular_time:
            user_dict["regular_time"] = datetime.strptime(self.regular_time + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
        if self.quit_time:
            user_dict["quit_time"] = datetime.strptime(self.quit_time + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
        if company_dict:
            user_dict["company"] = company_dict
        if department_dict:
            user_dict["department"] = department_dict
        if system_dict:
            user_dict["system"] = system_dict
        if role_dict:
            user_dict["role"] = role_dict
        query = {"username": self.username}
        yield g_motor_db.sys_user.update(query, user_dict, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def update_user(self):
    try:
        company_dict = {}
        department_dict = {}
        system_dict = {}
        role_dict = {}
        for company in self.company_list:
            temp = tuple(eval(company))
            company_dict[temp[0]] = temp[1]
        for department in self.department_list:
            temp = tuple(eval(department))
            department_dict[temp[0]] = temp[1]
        for system in self.system_list:
            temp = tuple(eval(system))
            system_dict[temp[0]] = temp[1]
        for role in self.role_list:
            temp = tuple(eval(role))
            role_dict[temp[0]] = temp[1]
        user_dict = {
            "tell_phone": self.tell_phone,
            "user_real_name": self.user_real_name,
            "email": self.email,
            "department": self.department,
            "position": self.position,
            "sex": self.sex,
            "age": self.age,
            "address": self.address,
            "status": self.status,
            "review": self.review,
            "emergency_contact": {
                "name": self.emergency_contact_name,
                "tell_phone": self.emergency_contact_tell_phone,
                "address": self.emergency_contact_address,
            },
            "last_update_time": datetime.now(),
        }
        if self.password:
            salt = hashlib.md5(self.username.encode('utf-8')).hexdigest()
            hash_password = hashlib.sha256((self.password + salt).encode('utf-8')).hexdigest()
            user_dict["password"] = hash_password
        if self.entry_time:
            user_dict["entry_time"] = datetime.strptime(self.entry_time + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
        if self.regular_time:
            user_dict["regular_time"] = datetime.strptime(self.regular_time + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
        if self.quit_time:
            user_dict["quit_time"] = datetime.strptime(self.quit_time + " 00:00:00", "%Y-%m-%d %H:%M:%S"),
        if company_dict:
            user_dict["company"] = company_dict
        if department_dict:
            user_dict["department"] = department_dict
        if system_dict:
            user_dict["system"] = system_dict
        if role_dict:
            user_dict["role"] = role_dict
        query = {"username": self.username}
        yield g_motor_db.sys_user.update(query, {"$set": user_dict}, upsert=True)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_user_one(self):
    try:
        query = {"username": self.username}
        yield g_motor_db.sys_user.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def del_user_list(self):
    try:
        query = {"username": {"$in": self.username_list}}
        yield g_motor_db.sys_user.remove(query)
        return 1
    except:
        logger.error(traceback.format_exc())
        return ""


