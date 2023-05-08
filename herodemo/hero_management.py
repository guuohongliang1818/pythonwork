# 姓名：郭宏亮
# 时间：2023/5/7 18:08
class HeroManagement:

    def __init__(self):
        self.hero_list = []

    def update_hero(self, hero_name, hero_volume):

        for i in self.hero_list:
            if hero_name == i.get("name"):
                i.update({"volume": hero_volume})
                return i
        return False

    def delete_hero(self, hero_name):
        for i in self.hero_list:
            if hero_name == i.get("name"):
                self.hero_list.remove(i)
                return True
        return False

    def create_hero(self, hero_name, hero_volume, hero_power):
        if not isinstance(hero_name, str):
            return False

        if not isinstance(hero_volume, int) or isinstance(hero_volume, bool) or hero_volume <= 0 or hero_volume >= 100:
            return False

        if not isinstance(hero_power, int) or isinstance(hero_power, bool) or hero_power <= 0:
            return False

        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        self.hero_list.append(hero_info)
        return True

    def find_hero(self, hero_name):
        for i in self.hero_list:
            if hero_name == i.get("name"):
                return i
        return False


if __name__ == '__main__':
    hero_management = HeroManagement()
    hero_management.create_hero(100, 12, 12)
    res = hero_management.find_hero(100)
    print("res=", res)
    print(not res)
