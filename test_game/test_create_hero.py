# 姓名：郭宏亮
# 时间：2023/5/7 19:33
import allure
import pytest

# 姓名：郭宏亮
# 时间：2023/5/7 18:42
# 实例化类
from herodemo.hero_management import HeroManagement


# 解决方案：如果测试步骤与断言全部一样，只有输入的数据不一样，就可以使用参数化
@pytest.mark.parametrize("name,volume,power", [
    ("张三", 23, 23),
    ("李四", 25, 25),
    ("王五", 23, 66)
])
@allure.title("成功生成英雄")
def test_create_hero_success(name, volume, power):
    # print(f"{name}，{volume}，{power}")
    hero_management = HeroManagement()
    hero_management.create_hero(name, volume, power)
    res = hero_management.find_hero(name)
    assert res
    assert res.get("name") == name
    assert res.get("volume") == volume
    assert res.get("power") == power


@pytest.mark.parametrize("volume", [0, 100], ids=["边界为0", "边界为100"])
@allure.title("失败生成英雄")
def test_create_hero3(volume):
    hero_management = HeroManagement()
    hero_management.create_hero("zhangsan", volume, 20)
    res = hero_management.find_hero("zhangsan")
    assert not res


@pytest.mark.parametrize("name", ["张三", "李四"])
@pytest.mark.parametrize("volume", [23, 44])
@pytest.mark.parametrize("power", [12, 67])
@allure.title("笛卡尔积")
def test_create_hero4(name, volume, power):
    print(f"{name},{volume},{power}")
    # hero_management = HeroManagement()
    # hero_management.create_hero("zhangsan", 100, 20)
    # res = hero_management.find_hero("zhangsan")
    # assert not res
