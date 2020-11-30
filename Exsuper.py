# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)# super는 셀프를 쓰지 않는다.
#         self.location = location


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__() # super는 다중 상속시 맨 처음 클래스만 상속됨
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽 생성
dropship = FlyableUnit()