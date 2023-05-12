# 姓名：郭宏亮
# 时间：2023/5/12 16:40

import pytest

# 定义一组测试数据
test_user_data = [1, 2]


@pytest.fixture(scope="module")
def login(request):
    user = request.param + 100
    print(f"账户{user}")
    return user


# indire=True标识login是个函数，只是在这被用作了参数
@pytest.mark.invalid
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    a = login
    print(f"用例中的login用户{a}")
    pass
