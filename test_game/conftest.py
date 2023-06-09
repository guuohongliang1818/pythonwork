# 姓名：郭宏亮
# 时间：2023/5/7 20:24
# 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
import pytest

from test_game.test_create_hero_homework_01 import Utils


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")
