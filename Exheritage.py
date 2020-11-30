class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

        #공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
         Unit.__init__(self, name, hp)
         self.damage = damage
