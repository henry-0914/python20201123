# 두개의 클래스를 부모로부터 상속받는 개념

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}시 방향으로 날아갑니다. [속도 {2}"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnint, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUint.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
# 발키리 유닛 생성
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")