# 姓名：郭宏亮
# 时间：2023/8/2 23:14
all_val = {'VAR_TOKEN': "12345"}
d = {'token': "all_val['VAR_TOKEN']"}
value = eval(d['token'])
# print(value)
str_d = str(d)
print(type(str_d))
print("all_val['sss']" in str_d)
print(bool(0))
