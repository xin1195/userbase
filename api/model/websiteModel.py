#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/23.
import hashlib
import traceback
from time import time

from tornado import gen

from setting import logger


@gen.coroutine
def get_website_list(self):
    """
    :param self:
    :return:
    """
    try:
        query = {}
        show = {"_id": 0}
        website_list = yield self.mongodb.website.find(query, show)
        print("website_list", website_list)
        return website_list
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def create_website(self):
    """
    :param self:
    :return:
    """
    try:
        query = {}
        show = {"_id": 0}
        website_list = yield self.mongodb.website.find(query, show)
        return website_list
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def update_website(self):
    """
    :param self:
    :return:
    """
    try:
        query = {}
        show = {"_id": 0}
        website_list = yield self.mongodb.website.find(query, show)
        return website_list
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def disable_website(self):
    """
    :param self:
    :return:
    """
    try:
        query = {}
        show = {"_id": 0}
        website_list = yield self.mongodb.website.find(query, show)
        return website_list
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def search_website(self):
    """
    :param self:
    :return:
    """
    try:
        query = {}
        show = {"_id": 0}
        website_list = yield self.mongodb.website.find(query, show)
        return website_list
    except:
        logger.error(traceback.format_exc())
        return ""


@gen.coroutine
def post_website(self):
    """
    :param self:
    :return:
    """
    try:
        query = {"website_code": self.website_code}
        data = {
            "website_code": self.website_code,
            "website_name": self.website_name,
            "website_domain": self.website_domain,
            "website_next": self.website_next
        }
        if self.action == "add":
            show = {"_id": 0}
            website = yield self.mongodb.website.find_one(query, show)
            if website:
                return 10, "error", "website_code is exist"
            else:
                auth_key = create_auth_key(self.website_code)
                data["auth_key"] = auth_key
        yield self.mongodb.website.update(query, {"$set": data}, upsert=True)
        return 0, "success", "create ok"
    except:
        logger.error(traceback.format_exc())
        return 1, "error", "function error"


@gen.coroutine
def update_auth_key(self):
    """
    :param self:
    :return:
    """
    try:
        auth_key = yield create_auth_key(self.website_code)
        if auth_key:
            query = {"website_code": self.website_code}
            data = {
                "auth_key": auth_key,
            }
            yield self.mongodb.website.update(query, {"$set": data}, upsert=True)
            return 0, "success", "create ok"
        else:
            return 11, "error", "create_auth_key error"
    except:
        logger.error(traceback.format_exc())
        return 1, "error", "function error"


@gen.coroutine
def create_auth_key(website_code):
    try:
        salt = time()
        auth_key = hashlib.sha1((str(website_code) + str(salt)).encode('utf-8')).hexdigest()
        return auth_key
    except:
        logger.error(traceback.format_exc())
        return "5d3b8b3f05cd493fcc72541e0c9711f28241dc56"
