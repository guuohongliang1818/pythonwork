# 姓名：郭宏亮
# 时间：2023/8/6 10:39
import deepdiff
from _decimal import Decimal

t1 = [[[1.0]]]
t2 = [[[20.0]]]
print(deepdiff.DeepDiff(t1, t2, ignore_order=True, cutoff_distance_for_pairs=0.3))
print(deepdiff.DeepDiff(t1, t2, ignore_order=True, cutoff_distance_for_pairs=0.2))
print(deepdiff.DeepDiff(t1, t2, ignore_order=True, cutoff_distance_for_pairs=0.1))
print("==================================")
print(deepdiff.DeepDiff(b'hello', 'hello'))
print(deepdiff.DeepDiff(b'hello', 'hello', ignore_string_type_changes=True))
print("==================================")
t3 = Decimal("10.01")
t4 = 10.01
print(deepdiff.DeepDiff(t3, t4))
print(deepdiff.DeepDiff(t3, t4, ignore_numeric_type_changes=True))
print("==================================")
t5 = 99
t6 = 99.0
print(deepdiff.DeepDiff(t5, t6))
print(deepdiff.DeepDiff(t5, t6, ignore_numeric_type_changes=True))
