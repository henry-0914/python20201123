# 당신의 학교는 파이썬 코딩 대회를 주최함
# 참석률을 높이기 위해 뎃글 이벤트 실시
# 추첨을 통해 1명 : 치킨, 3명 : 커피쿠폰
# 추첨 프로그램을 작성하시오

# rule 1. 20명 작성, 아이더어 1~ 20개 사이
# rule 2. 무작위 추첨, 중복 불가
# rule 3. random 모듈의 shuffle과 sample을 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 : 1
# 커피 : [2,3,4]
# -- 축하합니다--

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


from random import *
users = range(1, 21)
print(type(users))
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축합니다 --")