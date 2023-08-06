# 姓名：郭宏亮
# 时间：2023/8/6 10:16
import deepdiff

dict1 = {
    'code': 0,
    'message': '成功',
    'data': {
        'total': 28,
        'id': 123
    }
}

dict2 = {
    'code': 0,
    'message': '成功',
    'data': {
        'total': 29,
    }
}

print(deepdiff.DeepDiff(dict1, dict2))
