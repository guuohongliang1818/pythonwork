# 姓名：郭宏亮
# 时间：2023/5/8 8:45
import allure
import pytest
from herodemo.hero_management import HeroManagement


def isint():
    a = 0
    b = 1
    c = -1
    d = 12.2
    e = False
    f = "89078"
    print("a", isinstance(a, int) and not isinstance(a, bool))
    print("b", isinstance(b, int) and not isinstance(b, bool))
    print("c", isinstance(c, int) and not isinstance(c, bool))
    print("d", isinstance(d, int) and not isinstance(d, bool))
    print("e", isinstance(e, int) and not isinstance(e, bool))
    print("f", isinstance(f, int) and not isinstance(f, bool))


@pytest.mark.parametrize("power", [50, 500, 5000])
@pytest.mark.parametrize("volume", [1, 2, 98, 99])
@pytest.mark.parametrize("name", ["张三", "jinx", "807834167", "123@qq.com"])
@allure.title("创建英雄成功的测试用例")
@allure.step("创建英雄成功的测试用例")
def test_create_hero_success(name, volume, power):
    with allure.step("创建英雄成功的测试用例"):
        hero_management = HeroManagement()
        hero_management.create_hero(name, volume, power)
        res = hero_management.find_hero(name)
        print(res)
        assert res.get("name") == name
        assert res.get("volume") == volume
        assert res.get("power") == power


# 姓名不符合要求，姓名为整数，小数，或boolean
@pytest.mark.parametrize("power", [50])
@pytest.mark.parametrize("volume", [98])
@pytest.mark.parametrize("name", [100, 101.1, False], ids=["姓名为整数", "姓名为浮点数", "姓名为布尔值"])
@allure.title("创建英雄失败的测试用例-姓名不符合要求")
def test_create_hero_fail_for_name(name, volume, power):
    hero_management = HeroManagement()
    hero_management.create_hero(name, volume, power)
    res = hero_management.find_hero(name)
    assert not res


# 血量不符合要求，血量为边界值，负数，小数，字符串或boolean


@pytest.mark.parametrize("power", [500])
@pytest.mark.parametrize("volume", [0, 100, 52.3, -20, "123", "qe231", False],
                         ids=["血量为边界值0", "血量为边界值100", "血量为浮点数", "血量为负数", "血量为数字字符串",
                              "血量为字符串", "血量为布尔值"])
@pytest.mark.parametrize("name", ["jinx"])
@allure.title("创建英雄失败的测试用例-血量不符合要求")
def test_create_hero_fail_for_volume(name, volume, power):
    hero_management = HeroManagement()
    hero_management.create_hero(name, volume, power)
    res = hero_management.find_hero(name)
    assert not res


# 攻击力不符合要求，攻击力为边界值，负数，小数，字符串或boolean


@pytest.mark.parametrize("power", [0, -1, 444.4, "123", "qe231", False],
                         ids=["攻击力为边界值0", "攻击力为负数", "攻击力为浮点数", "攻击力为数字字符串",
                              "攻击力为字符串", "攻击力为布尔值"])
@pytest.mark.parametrize("volume", [98])
@pytest.mark.parametrize("name", ["jinx"])
@allure.title("创建英雄失败的测试用例-攻击力不符合要求")
def test_create_hero_fail_for_power(name, volume, power):
    hero_management = HeroManagement()
    hero_management.create_hero(name, volume, power)
    res = hero_management.find_hero(name)
    assert not res

# @pytest.mark.parametrize("power", [0, -1, 444.4, "123", "qe231", False],
#                          ids=["边界值0", "负数", "浮点数", "数字字符串", "字符串", "布尔值"])
# @pytest.mark.parametrize("volume", [0, 100, 52.3, -20, "123", "qe231", False],
#                          ids=["边界值0", "边界值100", "浮点数", "负数", "数字字符串", "字符串", "布尔值"])
# @pytest.mark.parametrize("name", [100, 101.1, False], ids=["整数", "小数", "布尔值"])
# @allure.title("创建英雄失败的测试用例-攻击力不符合要求")
# def test_create_hero_fail_for_name_volume_power(name, volume, power):
#     hero_management = HeroManagement()
#     hero_management.create_hero(name, volume, power)
#     res = hero_management.find_hero(name)
#     assert not False
