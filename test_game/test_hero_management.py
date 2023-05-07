# 姓名：郭宏亮
# 时间：2023/5/7 18:42
# 实例化类
from herodemo.hero_management import HeroManagement

hero_management = HeroManagement()


def setup_function():
    print("创建英雄")
    hero_management.create_hero("zhangsan", 20, 20)


def test_update_hero():
    hero_management.update_hero("zhangsan", 80)
    res = hero_management.find_hero("zhangsan")
    assert res.get("volume") == 80


def test_delete_hero():
    hero_management.delete_hero("zhangsan")
    res = hero_management.find_hero("zhangsan")
    print("delete=", res)
    assert not res


def test_create_hero():
    res = hero_management.find_hero("zhangsan")
    assert res.get("name") == "zhangsan"
    assert res.get("volume") == 20
    assert res.get("power") == 20


def test_find_hero():
    res = hero_management.find_hero("zhangsan")
    assert res.get("name") == "zhangsan"
