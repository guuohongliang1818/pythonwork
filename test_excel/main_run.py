# 姓名：郭宏亮
# 时间：2023/7/30 15:38
import os

import pytest

if __name__ == '__main__':
    pytest.main(["-s", "./test_create_hero_homework.py", "--alluredir", "./result", "--clean-alluredir"])
    os.system("allure generate ./result -o ./report-allure/ --clean")
