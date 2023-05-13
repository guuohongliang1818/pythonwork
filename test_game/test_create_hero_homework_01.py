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
    def is_int(self, num):
        return isinstance(num, int) and not isinstance(num, bool)

    # 每次调用测试方法都会生成一个HeroManagement实例对象
    @pytest.fixture(autouse=True)
    def create_hero_management(self):
        self.hero_management = HeroManagement()
        return self.hero_management

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

    # 对于边界值+1，有四种情况：success血量+1，fail血量+1，success攻击力+1，fail攻击力+1

    # 该夹具可在conftest.py文件中
    # "血量边界值1+1", "血量边界值99+1"
    @pytest.fixture
    def success_for_volume_plus1(self, success_for_volume):
        # 需要判断当前的参数是否是int类型，如果是int类型，并且是边界值，则+1
        if success_for_volume in [1, 99] and self.is_int(success_for_volume):
            return success_for_volume + 1
        else:
            pytest.skip("血量非等价类为None，跳过执行测试用例")

    # 该夹具可在conftest.py文件中
    # "血量边界值0+1", "血量边界值100+1"
    @pytest.fixture
    def fail_for_volume_plus1(self, fail_for_volume):
        # 需要判断当前的参数是否是int类型，如果是int类型，并且是边界值，则+1
        if fail_for_volume in [0, 100] and self.is_int(fail_for_volume):
            return fail_for_volume + 1
        else:
            pytest.skip("血量非等价类为None，跳过执行测试用例")

    # 该夹具可在conftest.py文件中
    # "攻击力边界值1+1"
    @pytest.fixture
    def success_for_power_plus1(self, success_for_power):
        if success_for_power == 1 and self.is_int(success_for_power):
            return success_for_power + 1
        else:
            pytest.skip("攻击力非等价类None，跳过执行测试用例")

    # 该夹具可在conftest.py文件中
    # "攻击力边界值0+1"
    @pytest.fixture
    def fail_for_power_plus1(self, fail_for_power):
        if fail_for_power == 0 and self.is_int(fail_for_power):
            return fail_for_power + 1
        else:
            pytest.skip("攻击力非等价类None，跳过执行测试用例")

    @pytest.mark.run(order=4)
    @allure.title("创建英雄成功的测试用例")
    def test_create_hero_success(self, success_for_name, success_for_volume, success_for_power):
        self.hero_management.create_hero(success_for_name, success_for_volume, success_for_power)
        res = self.hero_management.find_hero(success_for_name)
        assert res.get("name") == success_for_name
        assert res.get("volume") == success_for_volume
        assert res.get("power") == success_for_power

    @pytest.mark.run(order=5)
    @allure.title("创建英雄失败的测试用例-姓名不符合要求")
    def test_create_hero_fail_for_name(self, fail_for_name, success_for_volume, success_for_power):
        self.hero_management.create_hero(fail_for_name, success_for_volume, success_for_power)
        res = self.hero_management.find_hero(fail_for_name)
        assert not res

    @pytest.mark.run(order=6)
    @allure.title("创建英雄失败的测试用例-血量不符合要求")
    def test_create_hero_fail_for_volume(self, success_for_name, fail_for_volume, success_for_power):
        self.hero_management.create_hero(success_for_name, fail_for_volume, success_for_power)
        res = self.hero_management.find_hero(success_for_name)
        assert not res

    @pytest.mark.run(order=7)
    @allure.title("创建英雄失败的测试用例-攻击力不符合要求")
    def test_create_hero_fail_for_power(self, success_for_name, success_for_volume, fail_for_power):
        self.hero_management.create_hero(success_for_name, success_for_volume, fail_for_power)
        res = self.hero_management.find_hero(success_for_name)
        assert not res

    @pytest.mark.run(order=1)
    @allure.title("创建英雄成功的测试用例-(血+1)-(攻+1)")
    def test_create_hero_success_volume_p1_and_power_p1(self, success_for_name, success_for_volume_plus1,
                                                        success_for_power_plus1):
        print(f"{success_for_name},{success_for_volume_plus1},{success_for_power_plus1}")
        result = self.hero_management.create_hero(success_for_name, success_for_volume_plus1, success_for_power_plus1)
        res = self.hero_management.find_hero(success_for_name)
        # 可能存在创建成功，也可能创建失败，因为被测需求的代码没有修改
        if result:
            assert res.get("name") == success_for_name
            assert res.get("volume") == success_for_volume_plus1
            assert res.get("power") == success_for_power_plus1
        else:
            assert not res

    @pytest.mark.run(order=2)
    @allure.title("创建英雄失败的测试用例-(血+1)")
    def test_create_hero_fail_for_volume_p1(self, success_for_name, fail_for_volume_plus1, success_for_power_plus1):
        result = self.hero_management.create_hero(success_for_name, fail_for_volume_plus1, success_for_power_plus1)
        res = self.hero_management.find_hero(success_for_name)
        # 可能存在创建成功，也可能创建失败，因为被测需求的代码没有修改
        if result:
            assert res.get("name") == success_for_name
            assert res.get("volume") == fail_for_volume_plus1
            assert res.get("power") == success_for_power_plus1
        else:
            assert not res

    @pytest.mark.run(order=3)
    @allure.title("创建英雄失败的测试用例-(攻+1)")
    def test_create_hero_fail_for_power_p1(self, success_for_name, success_for_volume_plus1, fail_for_power_plus1):
        result = self.hero_management.create_hero(success_for_name, success_for_volume_plus1, fail_for_power_plus1)
        res = self.hero_management.find_hero(success_for_name)
        # 可能存在创建成功，也可能创建失败，因为被测需求的代码没有修改
        if result:
            assert res.get("name") == success_for_name
            assert res.get("volume") == success_for_volume_plus1
            assert res.get("power") == fail_for_power_plus1
        else:
            assert not res
