python = "Python is Amazing"
print(python.lower())
print(python.upper())

print(python[0].isupper())

print(len(python))

print(python.replace("Python", "Java"))

# 특정문자열 찾기
index = python.index("n")
print(index)

index = python.index("n", index + 1) # 첫번째 찾은 n 이후 2번째 n 찾기
print(index)

print(python.find("java")) #원하는 값이 없으면 -1 리턴
# 뒤에 코드가 있으면 그대로 실행
#print(python.index("java")) # 오류 리턴
# 뒤에 코드가 있으면 실행 안됨

print(python.count("n"))


