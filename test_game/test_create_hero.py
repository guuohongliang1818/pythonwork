# 姓名：郭宏亮
# 时间：2023/5/7 19:33
import allure
import pytest
# 姓名：郭宏亮
# 时间：2023/5/7 18:42
# 实例化类
from herodemo.hero_management import HeroManagement
from test_demo.utils import Utils


class TestCreateHero:
    # 类级，只在类中前后运行一次
    def setup_class(self):
        print("类级别--这是测试类的前置处理")

    def teardown_class(self):
        print("类级别--这是测试类的后置处理")

    def setup_method(self):
        print("方法级别--这是测试类的前置处理")

    def teardown_method(self):
        print("方法级别--这是测试类的前置处理")

    # 解决方案：如果测试步骤与断言全部一样，只有输入的数据不一样，就可以使用参数化
    @pytest.mark.web
    @pytest.mark.parametrize("name,volume,power", [
        ("张三", 23, 23),
        ("李四", 25, 25),
        ("王五", 23, 66)
    ])
    @allure.title("成功生成英雄")
    def test_create_hero_success(self, name, volume, power):
        # print(f"{name}，{volume}，{power}")
        hero_management = HeroManagement()
        hero_management.create_hero(name, volume, power)
        res = hero_management.find_hero(name)
        assert res
        assert res.get("name") == name
        assert res.get("volume") == volume
        assert res.get("power") == power

    @pytest.mark.P0
    @pytest.mark.parametrize("volume", [0, 100], ids=["边界为0", "边界为100"])
    @allure.title("失败生成英雄")
    def test_create_hero3(self, volume):
        hero_management = HeroManagement()
        hero_management.create_hero("zhangsan", volume, 20)
        res = hero_management.find_hero("zhangsan")
        assert not res

    @pytest.mark.P0
    @pytest.mark.parametrize("name", ["张三", "李四"])
    @pytest.mark.parametrize("volume", [23, 44])
    @pytest.mark.parametrize("power", [12, 67])
    @allure.title("笛卡尔积")
    def test_create_hero4(self, name, volume, power):
        print(f"{name},{volume},{power}")
        # hero_management = HeroManagement()
        # hero_management.create_hero("zhangsan", 100, 20)
        # res = hero_management.find_hero("zhangsan")
        # assert not res

    @pytest.mark.P0
    @pytest.mark.parametrize("power", Utils.load_yaml("./hero_info.yaml").get("power"))
    @pytest.mark.parametrize("volume", Utils.load_yaml("./hero_info.yaml").get("volume"))
    @pytest.mark.parametrize("name", Utils.load_yaml("./hero_info.yaml").get("name"))
    @allure.title("笛卡尔积")
    def test_create_hero5(self, name, volume, power):
        print(f"{name},{volume},{power}")

