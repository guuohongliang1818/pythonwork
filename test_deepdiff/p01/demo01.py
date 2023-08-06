# 姓名：郭宏亮
# 时间：2023/8/6 10:09
import deepdiff

with open("a.txt", "r", encoding="utf-") as file1:
    f1 = file1.read()

with open("b.txt", "r", encoding="utf-") as file2:
    f2 = file2.read()

print(f1)
print(f2)
print(deepdiff.DeepDiff(f1, f2))
