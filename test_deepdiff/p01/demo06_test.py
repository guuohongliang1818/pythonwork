# 姓名：郭宏亮
# 时间：2023/8/6 12:06
from deepdiff import DeepDiff

t1 = {
    'Author': '展昭',
    'wechat': 'ZZ666'
}
t2 = {
    'Author': '展昭',
    'wechat': 'ZZ666',
    'Blog': 'https://www.hctestedu.com/'
}
t3 = {
    'Author': '展昭',
    'wechat': 'ZZ777'
}
t4 = {
    'Author': '展昭',
    'wechat': 777
}
t5 = [{
    'Author': '展昭',
    'wechat': 'ZZ666'
}]
# Key值不同
print("Key值不同:")
print(DeepDiff(t1, t3).pretty())
# Key新增
print("Key新增:")
print(DeepDiff(t1, t2).pretty())
# Key减少
print("Key减少:")
print(DeepDiff(t2, t1).pretty())

# Key值类型改变
print("Key值类型改变:")
print(DeepDiff(t1, t4).pretty())
# 结构不同
print("结构不同:")
print(DeepDiff(t1, t5).pretty())
# Key值相同
print("Key值相同:")
result = DeepDiff(t1, t1).pretty()
print(DeepDiff(t1, t1).pretty())
assert "" == result
