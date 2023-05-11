# 姓名：郭宏亮
# 时间：2023/5/10 19:52
import pytest
import yaml

from test_demo.utils import Utils


def test_yaml1():
    with open("./volume.yaml", "r", encoding="utf-8") as file:
        # 将yaml文件的内容转成python数据结构
        volume = yaml.safe_load(file)
    print(volume)


def test_yaml2():
    with open("../test_game/test_create_hero_data.yaml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    print(data)


@pytest.mark.parametrize("volume", Utils.load_yaml("./volume.yaml"))
def test_yaml3(volume):
    print(f"volume:{volume}")
