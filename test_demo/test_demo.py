# 姓名：郭宏亮
# 时间：2023/5/7 17:29
# 如果没有使用pytest执行，就会当成正常的行数运行

def demo():
    return True


def setup_function():
    print("setup执行了")


def teardown_function():
    print("teardown执行了")


def test_demo():
    print("1234")
    assert 1 == 1
    assert 1 == 2
    assert 1 in [1, 2, 3]
    assert demo()


def test_demo2():
    print("4567")
    assert 1 == 1
