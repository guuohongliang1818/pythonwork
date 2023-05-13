# 姓名：郭宏亮
# 时间：2023/5/13 23:03
import pytest


# 获取原始数据
@pytest.fixture(params=["zhangsan", 2, "李四", 4])
def data3(request):
    yield request.param


@pytest.fixture
def data_transform(data3):
    if isinstance(data3, str):
        pytest.skip("字符串跳过")
    else:
        yield data3 + 1


def test_data3(data3):
    assert True


def test_data_transform(data_transform):
    print("+1后的数据", data_transform)
