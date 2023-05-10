# 姓名：郭宏亮
# 时间：2023/5/10 21:24
import pytest


@pytest.fixture
def data():
    return [1, 2, 3]


# 有些时候需要对数据进行二次定制
# 有些时候需要使用原始数据信息
@pytest.fixture
def data_plus(data):
    lst = []
    for i in data:
        i = i + 1
        lst.append(i)
    return lst


# 夹具套夹具，夹具开关的应用场景
# 比如：已有1000条用例数据，模块A使用，但是你不能动
# 如果想要复用夹具的逻辑，就可以使用套用夹具
# 如果有的场景要求数据+1，有的场景不要求数据+1，可以夹具开关
@pytest.fixture
def data2():
    return ["a", "b", "c"]


@pytest.fixture(autouse=False)
def merge_data(data, data2):
    data2.extend(data)


# 实现夹具的定制化
def test_data(data2):
    print(data2)
