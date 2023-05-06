# 姓名：郭宏亮
# 时间：2023/5/5 23:03
"""
1.在控制台输出提示信息，提醒用户选择对应的操作。
2.输入对应选项之后，则给出对应操作的提示信息。
"""

"""
    1. **创建英雄**     
    2. **查看英雄信息**     
    3. **修改英雄信息**     
    4. **删除英雄**     
    5. **退出系统**
    """
# 用于存放英雄
hero_list = []


def operate():
    print("""
        1. **创建英雄**     
        2. **查看英雄信息**     
        3. **修改英雄信息**     
        4. **删除英雄**     
        5. **退出系统**
        """)
    while True:
        num = int(input("请输入您要进行操作的数字编号："))
        if num == 1:
            createHero()
        elif num == 2:
            showHero()
        elif num == 3:
            updateHero()
        elif num == 4:
            deleteHero()
        elif num == 5:
            print("退出系统成功")
            break


def createHero():
    name = input("请输入英雄的名称：")
    # 校验英雄的名字是否存在
    for item in hero_list:
        if item.get("name") == name:
            print(f"姓名为{name}的英雄已经存在，创建失败。。。")
            return
    volume = int(input("请输入英雄的血量<正整数>："))
    fight = int(input("请输入英雄的战斗力<正整数>："))
    hero = {"name": name, "volume": volume, "fight": fight}
    hero_list.append(hero)
    print(f"姓名为{name}，血量为{volume}，战斗力为{fight}的英雄创建成功！！！")


def showHero():
    pass


def updateHero():
    pass


def deleteHero():
    pass


if __name__ == '__main__':
    operate()
