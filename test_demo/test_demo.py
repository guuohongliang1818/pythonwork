# 姓名：郭宏亮
# 时间：2023/5/7 17:29
# 如果没有使用pytest执行，就会当成正常的行数运行
import pytest


def demo():
    return True


# def setup_function():
#     print("setup执行了")
#
#
# def teardown_function():
#     print("teardown执行了")

@pytest.mark.run(order=3)
def test_demo():
    print("111")
    assert 1 == 1
    assert 1 in [1, 2, 3]
    assert demo()


@pytest.mark.run(order=1)
def test_demo2():
    print("222")
    assert 1 == 1


@pytest.mark.run(order=4)
def test_demo3():
    print("333")


@pytest.mark.run(order=2)
def test_demo4():
    print("4444")
