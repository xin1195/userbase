#!/usr/bin/env python3
# _*_coding:utf-8_*_
from tornado import web

from api.handler.departmentApiHandler import ApiDepartmentHandler
from api.handler.loginApiHandler import ApiLoginHandler
from api.handler.nodeApiHandler import ApiNodeCreateHandler, ApiNodeRetrieveHandler, ApiNodeUpdateHandler, ApiNodeDeleteHandler
from api.handler.roleApiHandler import ApiRoleCreateHandler, ApiRoleRetrieveHandler, ApiRoleUpdateHandler, ApiRoleDeleteHandler
from api.handler.systemApiHandler import ApiSystemCreateHandler, ApiSystemRetrieveHandler, ApiSystemUpdateHandler, ApiSystemDeleteHandler
from api.handler.testApiHandler import ApiTestHandler
from api.handler.tokenApiHandler import ApiTokenHandler
from api.handler.userApiHandler import ApiUserCreateHandler, ApiUserRetrieveHandler, ApiUserUpdateHandler, ApiUserDeleteHandler
from api.handler.userAuthApiHandler import ApiUserAuthHandler
from api.handler.websiteApiHandler import ApiWebsiteHandler, ApiWebsiteAuthKeyHandler

api_urls = [
    web.URLSpec(r"/api/test", ApiTestHandler, name="api_test"),
    # 系统登录、登出接口
    web.URLSpec(r"/api/login", ApiLoginHandler, name="api_login"),
    web.URLSpec(r"/api/token", ApiTokenHandler, name="api_token"),
    # 部门管理
    web.URLSpec(r"/api/department", ApiDepartmentHandler, name="api_department"),
    # 用户管理
    web.URLSpec(r"/api/user/retrieve", ApiUserRetrieveHandler, name="api_user_retrieve"),
    web.URLSpec(r"/api/user/create", ApiUserCreateHandler, name="api_user_create"),
    web.URLSpec(r"/api/user/update", ApiUserUpdateHandler, name="api_user_update"),
    web.URLSpec(r"/api/user/delete", ApiUserDeleteHandler, name="api_user_delete"),
    # 角色管理
    web.URLSpec(r"/api/role/create", ApiRoleCreateHandler, name="api_role_create"),
    web.URLSpec(r"/api/role/retrieve", ApiRoleRetrieveHandler, name="api_role_retrieve"),
    web.URLSpec(r"/api/role/update", ApiRoleUpdateHandler, name="api_role_update"),
    web.URLSpec(r"/api/role/delete", ApiRoleDeleteHandler, name="api_role_delete"),
    # 节点管理
    web.URLSpec(r"/api/node/create", ApiNodeCreateHandler, name="api_node_create"),
    web.URLSpec(r"/api/node/retrieve", ApiNodeRetrieveHandler, name="api_node_retrieve"),
    web.URLSpec(r"/api/node/update", ApiNodeUpdateHandler, name="api_node_update"),
    web.URLSpec(r"/api/node/delete", ApiNodeDeleteHandler, name="api_node_delete"),
    # 系统管理
    web.URLSpec(r"/api/system/create", ApiSystemCreateHandler, name="api_system_create"),
    web.URLSpec(r"/api/system/retrieve", ApiSystemRetrieveHandler, name="api_system_retrieve"),
    web.URLSpec(r"/api/system/update", ApiSystemUpdateHandler, name="api_system_update"),
    web.URLSpec(r"/api/system/delete", ApiSystemDeleteHandler, name="api_system_delete"),
    # 获取权限
    web.URLSpec(r"/api/user_auth", ApiUserAuthHandler, name="api_user_auth"),
    # 新增站点
    web.URLSpec(r"/api/website", ApiWebsiteHandler, name="api_website"),
    web.URLSpec(r"/api/auth_key", ApiWebsiteAuthKeyHandler, name="api_auth_key"),

]
