# 姓名：郭宏亮
# 时间：2023/8/2 21:30
import yaml


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as file:
        data_obj = yaml.load(file, Loader=yaml.FullLoader)

    return data_obj


def write_yaml(data, path):
    with open(path, "w", encoding="utf-8") as file:
        data_obj = yaml.dump(data, file, allow_unicode=True)


if __name__ == '__main__':
    result = load_yaml("../data/demo.yaml")
    print(result)
    # 字段的顺序会乱
    # write_yaml(result, "../data/test01.yaml")
