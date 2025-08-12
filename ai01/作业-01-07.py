# class Prentice:
#     def __init__(self, name, age, weapon):
#         self.name = name
#         self.age = age
#         self.weapon = weapon
#
#     def buddha(self):
#         print('念佛')
#
#     def do_pilgrimage(self):
#         print('取经')
#
#     def fight(self):
#         print('战斗')
#
# class Wk(Prentice):
#     def __init__(self, name, age, weapon, formula):
#         super(Wk, self).__init__(name, age, weapon)
#         self.formula = formula
#
#     def do_maigre(self):
#         print('吃斋')
#
#     def ext_devil(self):
#         print('降妖')
#
# class Zbj(Prentice):
#     def __init__(self, name, age, weapon, wife):
#         super(Zbj, self).__init__(name, age, weapon)
#         self.wife = wife
#
#     def hold_horse(self):
#         print('牵马')
#
# class Shs(Prentice):
#     def __init__(self, name, age, weapon, san_river):
#         super(Shs, self).__init__(name, age, weapon)
#         self.san_river = san_river
#
#     def pick_up_luge(self):
#         print('挑行李')
#
# wk = Wk('孙悟空', 18, '定海神针', '紧箍咒')
# zbj = Zbj('猪八戒', 19, '九齿钉耙', '翠兰')
# shs = Shs('沙和尚', 20, '禅杖', '流沙河')
#
# print(vars(wk))
# print(vars(zbj))
# print(vars(shs))


"""
人体关键点的描述plus版本扩展：
增加描述人体的：眼部关键点，手部关键点(分别创建3个即可)
然后分别遍历 眼部 和 手部 关键点
"""

class LandMark:
    def __init__(self, l_id, types, x, y):
        self.l_id = l_id
        self.types = types
        self.x = x
        self.y = y

class Person:
    def __init__(self, name, age, landmark):
        self.__name = name
        self.__age = age
        self.__landmark = landmark

    def add_landmark(self, landmark):
        self.__landmark.append(landmark)

    def show_landmark(self):
        for landmark in self.__landmark:
            print(landmark.l_id, landmark.types, landmark.x, landmark.y)

landmark_a = LandMark(0, '左眼', 10, 20)
landmark_b = LandMark(1, '右眼', 10, 30)
landmark_c = LandMark(2, '左手', 40, 60)
landmark_d = LandMark(3, '左手', 80, 60)

p = Person('李白', 20, [landmark_a, landmark_b, landmark_c, landmark_d])

p.show_landmark()