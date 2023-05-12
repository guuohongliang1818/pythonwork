# 姓名：郭宏亮
# 时间：2023/5/12 8:41
# 夹具套夹具，夹具开关的应用场景
# 比如：已有1000条用例数据，模块A使用，但是你不能动
# 如果想要复用夹具的逻辑，就可以使用套用夹具
# 如果有的场景要求数据+1，有的场景不要求数据+1，可以夹具开关
import pytest


@pytest.fixture
def data():
    yield [1, 2, 3]


@pytest.fixture
def data2():
    yield [4, 5, 6]


@pytest.fixture(autouse=True)
def merge_data(data, data2):
    print("死翘翘")
    data2.extend(data)


# 实现夹具的定制化
# @pytest.mark.parametrize("volume", data2)
def test_data(data2):
    print("*****", data2)
    # print("merge_data", merge_data)
