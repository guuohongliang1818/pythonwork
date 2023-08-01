# 姓名：郭宏亮
# 时间：2023/8/1 21:10
"""
getattr() 函数用于返回一个对象属性值
getattr(object,name[,default])
    参数
        object --对象
        name --字符串，对象属性
        default --默认名返回值，如果不提供该参数，在没有对应属性时，将触发attributeError
    返回值
        返回对象属性值
"""


# 实例一：简单对象，只有属性
class A:
    bar = 1


# 获取bar的值
a = A()
b = getattr(a, "bar")
print(b)
print(a.bar)

# 属性bar2不存在，此种写法会默认添加该属性并赋值
d = getattr(a, "bar2", 3)


# 该种写法，会报错：attributeError
# d1 = getattr(a, "bar3")


# 实例二： 常规对象，有方法
class B:
    def set(self, a, b):
        x = a
        a = b
        b = x
        print(a, b)

    def aaa(self):
        print("aaaa")


a = B()
c = getattr(a, "set")(a=1, b=2)
getattr(a, "aaa")()
