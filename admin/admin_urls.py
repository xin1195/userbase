#!/usr/bin/env python3
# _*_coding:utf-8_*_
from tornado import web

from admin.handler.authGroupHandler import AuthGroupHandler
from admin.handler.authNodeHandler import AuthNodeHandler
from admin.handler.companyHandler import CompanyHandler
from admin.handler.departmentHandler import DepartmentHandler
from admin.handler.indexHandler import IndexHandler
from admin.handler.loginHandler import LoginHandler
from admin.handler.userHandler import UserHandler
from admin.handler.websiteHandler import WebsiteHandler

admin_urls = [
    web.URLSpec(r"/", IndexHandler, name="admin_index"),
    web.URLSpec(r"/login", LoginHandler, name="admin_login"),
    web.URLSpec(r"/admin/user", UserHandler, name="admin_user"),
    web.URLSpec(r"/admin/company", CompanyHandler, name="admin_company"),
    web.URLSpec(r"/admin/department", DepartmentHandler, name="admin_department"),
    web.URLSpec(r"/admin/website", WebsiteHandler, name="admin_website"),
    web.URLSpec(r"/admin/auth_group", AuthGroupHandler, name="admin_auth_group"),
    web.URLSpec(r"/admin/auth_node", AuthNodeHandler, name="admin_auth_node"),
]
