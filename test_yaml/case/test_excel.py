# 姓名：郭宏亮
# 时间：2023/7/31 21:41
import pytest

from test_yaml.data_driver.excel_read import read_excel


@pytest.mark.parametrize("i", read_excel())
def test_01(i):
    print(i)


if __name__ == '__main__':
    pytest.main(["-s"])
