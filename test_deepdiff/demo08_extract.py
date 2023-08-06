# 姓名：郭宏亮
# 时间：2023/8/6 15:00
from deepdiff import extract

obj = {"a": [{'2': 'b'}, 3], "b": [4, 5]}
path = "root[a]"
print(extract(obj, path))
print(extract(obj, "root[a][0]['2']"))
print(extract(obj, "root['b'][0]"))
