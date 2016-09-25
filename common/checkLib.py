#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/24.


def check_user(user):
    if user:
        if user.get("add_time", ""):
            user["add_time"] = user.get("add_time").strftime("%Y-%m-%d %H:%M:%S")
        if user.get("last_update_time", ""):
            user["last_update_time"] = user.get("last_update_time").strftime("%Y-%m-%d %H:%M:%S")
        if user.get("entry_time", ""):
            user["entry_time"] = user.get("entry_time").strftime("%Y-%m-%d %H:%M:%S")
        if user.get("regular_time", ""):
            user["regular_time"] = user.get("regular_time").strftime("%Y-%m-%d %H:%M:%S")
        if user.get("quit_time", ""):
            user["quit_time"] = user.get("quit_time").strftime("%Y-%m-%d %H:%M:%S")
    return user
