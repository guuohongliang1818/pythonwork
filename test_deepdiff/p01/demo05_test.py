# 姓名：郭宏亮
# 时间：2023/8/6 10:58
from deepdiff import DeepDiff

t1 = {"name": "yanan", "pro": {"sh": "shandong", "city": ["zibo", "weifang"]}}
t2 = {"name": "changsha", "pro": {"sh": "shandong", "town": ["taian", "weifang"]}}
# tree视图具有遍历对象的功能，
# 可以看到哪些对象与哪些其他对象进行了比较
# text不会展示t1,t2节点的信息
ddiff = DeepDiff(t1, t2, view='tree')
print(ddiff)
print("=========================")
# 默认为text
ddiff = DeepDiff(t1, t2, view='text')
print(ddiff)
print("美化之后")
ddiff = DeepDiff(t1, t2, view='tree').pretty()
print(ddiff)
print("=========================")
# 默认为text
ddiff = DeepDiff(t1, t2, view='text').pretty()
print(ddiff)
