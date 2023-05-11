# 姓名：郭宏亮
# 时间：2023/5/10 20:07
import yaml


class Utils:
    @classmethod
    def load_yaml(cls, yaml_path):
        with open(yaml_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


def reader(func):
    def inner(*args):
        with open(args[0], "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        # result = func(*args)
        return yaml_data
    return inner


@reader
def read_yaml(yaml_path):
    pass


# inn = reader(read_yaml)

if __name__ == '__main__':
    # data = Utils.load_yaml("../test_game/hero_info.yaml")
    # print(data)
    lst = [1, 2, 3, 4, 5]
    print(lst[0])
    res = read_yaml("../test_game/test_create_hero_data.yaml")
    print(res)
