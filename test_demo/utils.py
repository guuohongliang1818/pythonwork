# 姓名：郭宏亮
# 时间：2023/5/10 20:07
import yaml


class Utils:
    @classmethod
    def load_yaml(cls, yaml_path):
        with open(yaml_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


def reader(yaml_path):

    with open(yaml_path, "r", encoding="utf-8") as file:
        yaml_data = yaml.safe_load(file)

    def inner():
        pass

    return inner


if __name__ == '__main__':
    data = Utils.load_yaml("../test_game/hero_info.yaml")
    print(data)
