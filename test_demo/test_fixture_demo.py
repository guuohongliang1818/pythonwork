# 姓名：郭宏亮
# 时间：2023/5/10 21:24
import pytest

from test_demo.utils import Utils


@pytest.fixture
def data():
    yield [1, 2, 3]


# 有些时候需要对数据进行二次定制
# 有些时候需要使用原始数据信息
@pytest.fixture
def data_plus(data):
    lst = []
    for i in data:
        i = i + 1
        lst.append(i)
    yield lst


# 夹具套夹具，夹具开关的应用场景
# 比如：已有1000条用例数据，模块A使用，但是你不能动
# 如果想要复用夹具的逻辑，就可以使用套用夹具
# 如果有的场景要求数据+1，有的场景不要求数据+1，可以夹具开关
@pytest.fixture
def data2():
    yield ["a", "b", "c"]


@pytest.fixture(autouse=False)
def merge_data(data, data2):
    print("死翘翘")
    data2.extend(data)


# 实现夹具的定制化
def test_data(data2):
    pass
    print("*****", data2)
    # print("merge_data", merge_data)


print("=========================================================================")


# 获取原始数据
@pytest.fixture(params=Utils.load_yaml("./volume.yaml"))
def data3(request):
    print("#############", request.param)
    yield request.param


# 创建新的集合
@pytest.fixture
def data_plus1():
    pass


# 数据+1之后放入到新的集合
@pytest.fixture(autouse=True)
def plus_one(data3):
    # print("+1得到数据", data3)
    yield data3 + 1
    # print("data3:", data3)


def test_data3(data3):
    print("+1后的数据", data3)


print("===========================================================================================")


@pytest.fixture(params=Utils.load_yaml("./volume.yaml"))
def data4(request):
    print("#############", request)
    yield request.param + 1


# 将家具作为函数的参数
def test_data4(data4):
    print("+1之后得到数据：", data4)
