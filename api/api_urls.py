#!/usr/bin/env python3
# _*_coding:utf-8_*_
from tornado import web

from api.controller.companyController import ApiCompanyCreateController, ApiCompanyRetrieveController, ApiCompanyUpdateController, ApiCompanyDeleteController
from api.controller.departmentController import ApiDepartmentCreateController, ApiDepartmentRetrieveController, ApiDepartmentUpdateController, ApiDepartmentDeleteController
from api.controller.loginController import ApiLoginController
from api.controller.nodeController import ApiNodeCreateController, ApiNodeRetrieveController, ApiNodeUpdateController, ApiNodeDeleteController
from api.controller.roleController import ApiRoleCreateController, ApiRoleRetrieveController, ApiRoleUpdateController, ApiRoleDeleteController
from api.controller.systemController import ApiSystemCreateController, ApiSystemRetrieveController, ApiSystemUpdateController, ApiSystemDeleteController
from api.controller.testController import ApiTestController
from api.controller.tokenController import ApiTokenController
from api.controller.userAuthController import ApiUserAuthController
from api.controller.userController import ApiUserCreateController, ApiUserRetrieveController, ApiUserUpdateController, ApiUserDeleteController

api_urls = [
    web.URLSpec(r"/api/test", ApiTestController, name="api_test"),
    # 系统登录、登出接口
    web.URLSpec(r"/api/login", ApiLoginController, name="api_login"),
    web.URLSpec(r"/api/token", ApiTokenController, name="api_token"),
    # 公司管理
    web.URLSpec(r"/api/company/create", ApiCompanyCreateController, name="api_company_create"),
    web.URLSpec(r"/api/company/retrieve", ApiCompanyRetrieveController, name="api_company_retrieve"),
    web.URLSpec(r"/api/company/update", ApiCompanyUpdateController, name="api_company_update"),
    web.URLSpec(r"/api/company/delete", ApiCompanyDeleteController, name="api_company_delete"),
    # 部门管理
    web.URLSpec(r"/api/department/create", ApiDepartmentCreateController, name="api_department_create"),
    web.URLSpec(r"/api/department/retrieve", ApiDepartmentRetrieveController, name="api_department_retrieve"),
    web.URLSpec(r"/api/department/update", ApiDepartmentUpdateController, name="api_department_update"),
    web.URLSpec(r"/api/department/delete", ApiDepartmentDeleteController, name="api_department_delete"),
    # 用户管理
    web.URLSpec(r"/api/user/retrieve", ApiUserRetrieveController, name="api_user_retrieve"),
    web.URLSpec(r"/api/user/create", ApiUserCreateController, name="api_user_create"),
    web.URLSpec(r"/api/user/update", ApiUserUpdateController, name="api_user_update"),
    web.URLSpec(r"/api/user/delete", ApiUserDeleteController, name="api_user_delete"),
    # 角色管理
    web.URLSpec(r"/api/role/create", ApiRoleCreateController, name="api_role_create"),
    web.URLSpec(r"/api/role/retrieve", ApiRoleRetrieveController, name="api_role_retrieve"),
    web.URLSpec(r"/api/role/update", ApiRoleUpdateController, name="api_role_update"),
    web.URLSpec(r"/api/role/delete", ApiRoleDeleteController, name="api_role_delete"),
    # 节点管理
    web.URLSpec(r"/api/node/create", ApiNodeCreateController, name="api_node_create"),
    web.URLSpec(r"/api/node/retrieve", ApiNodeRetrieveController, name="api_node_retrieve"),
    web.URLSpec(r"/api/node/update", ApiNodeUpdateController, name="api_node_update"),
    web.URLSpec(r"/api/node/delete", ApiNodeDeleteController, name="api_node_delete"),
    # 系统管理
    web.URLSpec(r"/api/system/create", ApiSystemCreateController, name="api_system_create"),
    web.URLSpec(r"/api/system/retrieve", ApiSystemRetrieveController, name="api_system_retrieve"),
    web.URLSpec(r"/api/system/update", ApiSystemUpdateController, name="api_system_update"),
    web.URLSpec(r"/api/system/delete", ApiSystemDeleteController, name="api_system_delete"),
    # 获取权限
    web.URLSpec(r"/api/user_auth", ApiUserAuthController, name="api_user_auth"),

]
