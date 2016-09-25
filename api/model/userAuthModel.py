#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by LiuXin 
# Time 2016/8/29.
import json
import traceback

from tornado import gen

from common.commonLib import set_node_to_redis, get_node_to_redis
from setting import g_motor_db, logger


@gen.coroutine
def get_user_auth(self):
    try:
        redis_data = get_node_to_redis(self.username)
        if redis_data:
            node_dict = json.loads(redis_data.decode())
        else:
            node_dict = {}
            role_id_list = []
            query = {"username": self.username, "system." + self.system: {"$exists": 1}}
            show = {"_id": 0, "username": 1, "role": 1}
            user = yield g_motor_db.sys_user.find_one(query, show)
            role_dict = user.get("role", "")
            for role_id, role_name in role_dict.items():
                role_id_list.append(role_id)
            cursor = g_motor_db.sys_role.find({"role_id": {"$in": role_id_list}}, {"_id": 0})
            while (yield cursor.fetch_next):
                role = cursor.next_object()
                node_dict.update(role.get("node"))
            set_node_to_redis(self.username, node_dict)
        return node_dict
    except:
        logger.error(traceback.format_exc())
        return {}

