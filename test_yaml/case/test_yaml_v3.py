# 姓名：郭宏亮
# 时间：2023/7/31 21:41
import allure
import pytest

from test_yaml.VAR import YAML_PATH, WRITE_PATH
from test_yaml.api_keyword.api_key import ApiKey

from test_yaml.data_driver.yaml_driver import load_yaml, write_yaml


# 在当前文件中，所有的用例执行之前运行一次

# @pytest.fixture(scope="class")
def setup_module():
    # 1.定义全局变量
    global ak, all_val, yaml_data
    # 实例化工具类
    ak = ApiKey()
    # 初始化excel文件
    yaml_data = []
    # 参数化变量存储字典临时数据库
    all_val = {}


def teardown_module():
    write_yaml(yaml_data, WRITE_PATH)


@pytest.mark.parametrize("data", load_yaml(YAML_PATH))
def test_01(data):
    # 动态生成用例标题
    if data["title"] is not None:
        allure.dynamic.title(data["title"])

    if data["story"] is not None:
        allure.dynamic.story(data["story"])

    if data["feature"] is not None:
        allure.dynamic.feature(data["feature"])

    if data["note"] is not None:
        allure.dynamic.description(data["note"])

    if data["level"] is not None:
        allure.dynamic.severity(data["level"])
    # ==========excel数据解析==========
    # print(data)
    try:
        # eval无法解析字典数据
        dict_data = {
            "url": data["url"] + data["apiPath"],
            "params": data["params"],
            "headers": data["headers"],
            data["dataType"]: data["data"]
        }
        if "all_val['VAR_TOKEN']" in str(dict_data):
            dict_data = eval(str(dict_data).replace("all_val['VAR_TOKEN']", all_val.get('VAR_TOKEN')))
    except BaseException as e:
        print("========实际结果=======")
        print("请求参数有误，请检查：", e)
        data["result"] = "请求参数有误，请检查"
    # print("data：", data)
    # 发起请求
    print("请求参数：", dict_data)
    # res = ak.post(url=dict_data.get("url"), params=dict_data.get("params"), json=dict_data.get(data[7]))
    res = ak.post(**dict_data)

    # 反射
    # res = getattr(ak, data[3])(**dict_data)
    print("请求返回：", res.text)

    # ================JSON提取器===================
    if data["jsonVar"] is not None:
        var_str = data["jsonVar"]
        print(var_str)
        # 用分号分割var_str字符串，并保存到列表
        var_str_list = var_str.split(";")
        print(var_str_list)
        # 获取json的表达式
        json_str = data["jsonPath"]
        json_str_list = json_str.split(";")
        print(json_str_list)

        for i in range(len(var_str_list)):
            # 获取json的引用名称
            key = var_str_list[i]
            # 获取表达式
            json_exp = json_str_list[i]

            # 获取报文中值
            value = ak.get_text(res.text, json_exp)

            # 形成字典对应的关系
            # 重要：将所有用例提取的key，value都保存起来
            all_val[key] = value
    # 结果检查
    print("all_val", all_val)
    # 实际结果
    try:
        result = None
        result = ak.get_text(res.text, data["validate"])
        print(result == data["expect"])
        if result == data["expect"]:
            data["result"] = "通过"
        else:
            data["result"] = "不通过"
    except:
        print("==============实际结果==============")
        print("预期结果的jsonpath表达式有误，请检查")
        data["result"] = "预期结果的jsonpath表达式有误，请检查"
    finally:
        yaml_data.append(data)
        assert result == data["expect"]


if __name__ == '__main__':
    pytest.main(["-s", "test_yaml_v3.py::test_01"])
