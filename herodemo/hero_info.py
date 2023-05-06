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
    fight = int(input("请输入英雄的攻击力<正整数>："))
    hero = {"name": name, "volume": volume, "fight": fight}
    hero_list.append(hero)
    print(f"姓名为{name}，血量为{volume}，攻击力为{fight}的英雄创建成功！！！")


def showHero():
    # name = input("请输入查看英雄名称：").strip(" ")
    if len(hero_list) != 0:
        # 展示所有英雄
        for item in hero_list:
            print(f"姓名：{item.get('name')}\t血量：{item.get('volume')}\t攻击力：{item.get('fight')}")
        # if name == "":
        #     for item in hero_list:
        #         print(f"姓名：{item.get('name')}\t血量：{item.get('volume')}\t攻击力：{item.get('fight')}")
        # else:
        #     for item in hero_list:
        #         if item.get("name") == name:
        #             print(f"姓名：{item.get('name')}\t血量：{item.get('volume')}\t攻击力：{item.get('fight')}")
        #             return
        #     print(f"您输入的{name}英雄名称未找到相关信息，请创建英雄。。。")
    else:
        print("暂时没有英雄，请创建英雄。。。")


def updateHero():
    if len(hero_list) != 0:
        name = input("请输入更新英雄名称：").strip(" ")
        if name == "":
            print("输入的英雄名称不能为空。。。")
            return
        else:
            for item in hero_list:
                if item.get("name") == name:
                    volume = int(input("请输入更新的血量<正整数>："))
                    # fight = int(input("请输入更新的攻击力<正整数>："))
                    """
                    item["volume"] = volume
                    item["fight"] = fight
                    或者采取如下更新API
                    """
                    item.update({"volume": volume})
                    print(f"姓名为{name}，血量为{volume}的英雄信息更新成功")
                    return
            print(f"您输入的{name}英雄名称未找到相关信息，请创建英雄。。。")
    else:
        print("暂时没有英雄，请创建英雄。。。")


def deleteHero():
    if len(hero_list) != 0:
        name = input("请输入删除英雄名称：").strip(" ")
        if name == "":
            print("输入的英雄名称不能为空。。。")
        else:
            for item in hero_list:
                if item.get("name") == name:
                    hero_list.remove(item)
                    print(f"姓名为{name}的英雄信息删除成功！！！")
                    return
            print(f"您输入的{name}英雄名称未找到相关信息。。。")
    else:
        print("暂时没有英雄。。。")


if __name__ == '__main__':
    operate()
