# 姓名：郭宏亮
# 时间：2023/8/6 14:52
from deepdiff import DeepSearch, grep

# 正则表达式这个点的应用场景比较多，当你事先对预期结果的值不能进行100%确定时，可以使用正则匹配实际值进行断言
obj = ["long somewhere", "string", 0, "somewhere great!"]
# 使用正则表达式
item = "some*"
ds = DeepSearch(obj, item, use_regexp=True)
print(ds)
# 大小写敏感
item = 'someWhere'
ds = DeepSearch(obj, item, case_sensitive=True)
print(ds)
item = 'some'
ds = DeepSearch(obj, item, case_sensitive=True)
print(ds)
# 强校验
item = 0
ds = DeepSearch(obj, item, strict_checking=True)
print(ds)
item = "0"
ds = DeepSearch(obj, item, strict_checking=True)
print(ds)

obj = ["long somewhere", "string", 0, "somewhere great!"]
item = "somewhere"
ds = obj | grep(item)
print(ds)
