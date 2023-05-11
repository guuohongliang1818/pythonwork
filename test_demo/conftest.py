# 姓名：郭宏亮
# 时间：2023/5/11 8:50
import pytest


@pytest.fixture(scope="function")
def data():
    return [56, "张三", False, 123.4]
