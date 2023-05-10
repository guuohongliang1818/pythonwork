# 姓名：郭宏亮
# 时间：2023/5/10 22:02
import pytest


@pytest.fixture
def data():
    print("这是用例执行之前的操作")
    # 类似于return，与return不同的是还会往后执行 （yield挂起）
    yield "hello world"
    print("我终于执行完了！！！！")


def test_data(data):
    print(data)
    print("这是我执行的测试信息。。。。")



