# 姓名：郭宏亮
# 时间：2023/5/11 8:40
import pytest


@pytest.fixture
def data():
    return [1, 2, 3]


class TestDemo1:

    def test_demo1(self, data):
        print(data)


class TestDemo2:

    def test_demo2(self, data):
        print(data)


class TestDemo3:

    def test_demo3(self, data):
        print(data)
