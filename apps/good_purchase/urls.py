# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from django.conf.urls import url
from django.urls import path

# from apps.tools.derive_excel import derive_excel
from ..tools import del_excel, derive_excel, import_cart_excel
# from apps.tools.del_excel import del_excel
# from apps.tools.import_excel import import_excel
from . import views

urlpatterns = (
    path("get_good_detail", views.get_good_detail),  # 商品详情
    path("get_shopping_cart", views.get_shopping_cart),  # 获取购物车信息
    path("delete_cart_goods", views.delete_cart_goods),  # 删除购物车信息
    path("update_cart_goods", views.update_cart_goods),  # 修改购物车数量信息
    path("add_cart_goods", views.add_cart_goods),  # 添加物资到购物车/更新购物车物资数量
    path("get_group_apply", views.get_group_apply),  # 获取组内物资表数据
    path("delete_group_apply", views.delete_group_apply),  # 删除组内物资表数据
    path("update_group_apply", views.update_group_apply),  # 更新组内物资表数据
    path("import_excel", import_cart_excel.import_cart_excel),  # 通过excel导入数据到部门所需物资
    path("derive_excel", derive_excel.derive_excel),  # 导出部门所需物资数据
    path("del_excel", del_excel.del_excel),  # 删除excel文件
    path("get_good_list", views.get_good_list),  # 获取商品列表
    path("get_good_type_list", views.get_good_type_list),  # 获取商品类别列表
    path("add_good", views.add_good),  # 新增商品信息
    path("update_good", views.update_good),  # 修改商品信息
    path("add_good_type", views.add_good_type),  # 新增商品类型信息
    path("down_good", views.down_good),  # 下架商品
    path("upload_img", views.upload_img),  # 上传图片
    path("get_withdraw_reason", views.get_withdraw_reason),  # 获取所有退回商品原因
    path("add_withdraw_apply", views.add_withdraw_apply),  # 提交退回商品申请
    url(r"^get_personal_goods/$", views.get_personal_goods),  # 获取个人物资接口
    path("get_good_status_list", views.get_good_status_list),  # 获取物资状态列表
    path('get_user_info', views.get_user_info),  # 获取用户信息
    path('edit_user_info', views.edit_user_info),  # 修改用户信息
    path('confirm_receipt', views.confirm_receipt),  # 确认收货
    path('get_good_code_list', views.get_good_code_list),  # 获取商品编码列表
    path('del_pics', views.del_pics)  # 删除图片
)
