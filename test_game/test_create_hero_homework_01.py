# 姓名：郭宏亮
# 时间：2023/5/12 8:55
import allure
import pytest
import yaml

from herodemo.hero_management import HeroManagement


class Utils:
    @classmethod
    def load_yaml(cls, yaml_path):
        with open(yaml_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


class TestHeroCreate:
    # 每次调用测试方法都会生成一个HeroManagement实例对象
    def setup_method(self):
        self.hero_management = HeroManagement()

    # 该夹具可在conftest.py文件中
    @pytest.fixture(params=Utils.load_yaml("./test_create_hero_data_01.yaml").get("success").get("for_name"))
    def success_for_name(self, request):
        yield request.param

    # 该夹具可在conftest.py文件中
    @pytest.fixture(params=Utils.load_yaml("./test_create_hero_data_01.yaml").get("success").get("for_volume"))
    def success_for_volume(self, request):
        yield request.param

    # 该夹具可在conftest.py文件中
    @pytest.fixture(params=Utils.load_yaml("./test_create_hero_data_01.yaml").get("success").get("for_power"))
    def success_for_power(self, request):
        yield request.param

    # 该夹具可在conftest.py文件中
    @pytest.fixture(params=Utils.load_yaml("./test_create_hero_data_01.yaml").get("fail").get("for_name"),
                    ids=Utils.load_yaml("./test_create_hero_data_01.yaml").get("fail").get("for_name_desc"))
    def fail_for_name(self, request):
        yield request.param

    # 该夹具可在conftest.py文件中
    @pytest.fixture(params=Utils.load_yaml("./test_create_hero_data_01.yaml").get("fail").get("for_volume"),
                    ids=Utils.load_yaml("./test_create_hero_data_01.yaml").get("fail").get("for_volume_desc"))
    def fail_for_volume(self, request):
        yield request.param

    # 该夹具可在conftest.py文件中
    @pytest.fixture(params=Utils.load_yaml("./test_create_hero_data_01.yaml").get("fail").get("for_power"),
                    ids=Utils.load_yaml("./test_create_hero_data_01.yaml").get("fail").get("for_power_desc"))
    def fail_for_power(self, request):
        yield request.param

    @allure.title("创建英雄成功的测试用例")
    def test_create_hero_success(self, success_for_name, success_for_volume, success_for_power):
        self.hero_management.create_hero(success_for_name, success_for_volume, success_for_power)
        res = self.hero_management.find_hero(success_for_name)
        assert res.get("name") == success_for_name
        assert res.get("volume") == success_for_volume
        assert res.get("power") == success_for_power

    @allure.title("创建英雄失败的测试用例-姓名不符合要求")
    def test_create_hero_fail_for_name(self, fail_for_name, success_for_volume, success_for_power):
        self.hero_management.create_hero(fail_for_name, success_for_volume, success_for_power)
        res = self.hero_management.find_hero(fail_for_name)
        assert not res

    @allure.title("创建英雄失败的测试用例-血量不符合要求")
    def test_create_hero_fail_for_volume(self, success_for_name, fail_for_volume, success_for_power):
        self.hero_management.create_hero(success_for_name, fail_for_volume, success_for_power)
        res = self.hero_management.find_hero(success_for_name)
        assert not res

    @allure.title("创建英雄失败的测试用例-攻击力不符合要求")
    def test_create_hero_fail_for_power(self, success_for_name, success_for_volume, fail_for_power):
        self.hero_management.create_hero(success_for_name, success_for_volume, fail_for_power)
        res = self.hero_management.find_hero(success_for_name)
        assert not res
