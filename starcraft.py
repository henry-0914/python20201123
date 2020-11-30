# 일반유닛
class Unit:
    def __init__(self, name, hp, speed)
    self.name = Name
    self.hp = hp
    self.speed = speed
    print("{0} 유닛이 생성되었습니다.".format(name))











# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# 마린 유닛 생성
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP : 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))




# 레이스 생성
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__("레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드(해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해체
            print("{0} :  클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else: #클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정 합니다.".format(self.name))
            self.clocked = False