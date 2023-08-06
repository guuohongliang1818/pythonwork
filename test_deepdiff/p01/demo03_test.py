# 姓名：郭宏亮
# 时间：2023/8/6 10:21
import pytest
import requests
from deepdiff import DeepDiff


class TestCase:
    expect = {
        'slideshow': {
            'author': 'Yours Truly',
            'date': 'date of publication11',
            'slides': [
                {
                    'title': 'Wake up to WonderWidgets!',
                    'type': 'all'
                },
                {
                    'items': ['Why <em>WonderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'],
                    'title': 'Overview',
                    'type': 'all'
                }
            ],
            'title': 'Sample Slide Show'
        }
    }

    def setup(self):
        # 返回字典格式报文
        self.response = requests.get('http://www.httpbin.org/json').json()
        print(self.response)

    def test_case_01(self):
        print("用例对比结果：")
        print(DeepDiff(self.response, self.expect))

    def test_case_02(self):
        print("用例对比结果：")
        print(DeepDiff(self.response['slideshow']['author'], 'Yours Truly1'))

    def test_case_03(self):
        print("比对结果：")
        print(DeepDiff(self.response, self.expect,
                       exclude_paths="root['slideshow']['date']"))


if __name__ == '__main__':
    pytest.main(['-s'])
