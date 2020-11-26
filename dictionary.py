cabinet = {3:"유재석", 10:"김재호"}
print(cabinet[3])
print(cabinet[10])

print(cabinet.get(3))

# print(cabinet[5]) # []로 사용하면 바로 프로그램 종료, 밑에 하이 실행 안됨
# print("hi")

print(cabinet.get(5)) # get 사용하면 none 출력되고 밑에 하이 실행됨
print(cabinet.get(5, "사용가능"))
print("hi")

# 캐비넷 번호가 존재하는지 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-10" : "김재호"}
print(cabinet["A-3"])
print(cabinet["B-10"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 탈퇴 손님 삭제
del cabinet["A-3"]
print(cabinet)

# key 번호만 출력
print(cabinet.keys())

# value 값만 출력
print(cabinet.values())

# key, value, 둘다 출력
print(cabinet.items())

#목욕탕 폐점 전체 클리어
cabinet.clear()
print(cabinet)


