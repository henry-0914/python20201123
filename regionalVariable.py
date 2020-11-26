# 지역변수 : 함수내에서만 사용 가능
# 전역변수 : 모든 공간에서 다 사용 가능

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun -soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
#checkpoint(2) # 두명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))