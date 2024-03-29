#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    这是接口关键字驱动类，用于提供自动化接口测试的关键字方法。
    主要是实现常用的关键字内容，并定义好所有的参数内容即可
    接口中常用关键字：
        1.各种模拟请求方法：Post/get/put/delete/header/....
        2.集合Allure，可添加@allure.step，这样在自动化执行的时候
        Allure报告可以直接捕捉相关的执行信息，让测试报告更详细
        3.根据需求进行断言封装：jsonpath、数据库断言
"""
import json
import logging
import allure
import jsonpath
import pymysql
import requests


# 工具类/关键字驱动类/基类
class ApiKey:
    @allure.step("发送get请求")
    def get(self, url, params=None, **kwargs):
        logging.info("发送get请求")
        return requests.get(url=url, params=params, **kwargs)

    @allure.step("发送post请求")
    def post(self, url, data=None, json=None, **kwargs):
        logging.info("发送post请求")
        return requests.post(url=url, data=data, json=json, **kwargs)

    # 基于jsonpath获取数据的关键字：用于提取所需要的内容
    # @allure.step("获取返回结果字典值")
    def get_text(self, response, key):
        """
        :param response: 响应报文，默认为json格式
        :param key: jsonpath的表达式
        :return:
        """
        dict_data = json.loads(response)
        value_list = jsonpath.jsonpath(dict_data, key)
        return value_list[0]

    @allure.step("数据库检查")
    def sql_check(self, sql):
        # 01建立连接
        conn = pymysql.connect(
            host="shop-xo.hctestedu.com",
            port=3306,
            user="api_test",
            password="Aa9999!",
            database="shopxo_hctested",
            charset="utf8mb4"
        )
        # 创建游标
        cmd = conn.cursor()
        # 执行sql语句
        cmd.execute(query=sql)
        # 获取查询结果
        result = cmd.fetchone()[0]
        # 关闭连接
        conn.close()
        return result


if __name__ == '__main__':
    ak = ApiKey()
    results = ak.sql_check("select username,'123' from sxo_admin")
    print(results)
