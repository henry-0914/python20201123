#건물
class BuildingUnint(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnint("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림 새로운 게임을 시작합니다.")

def game_over():
    pass
game_start()
game_over()