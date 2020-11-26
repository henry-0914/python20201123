# 중복 안됨, 순서 없음

my_set = {1,2,3,4,5}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java+python 둘다 가능)
print(java & python)
print(java.intersection(python))

# 합집함(java or python)
print(java | python)
print(java.union(python))

# 차집합(java -python)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람 늘어남(추가)
python.add("김태호")
print(python)

# java를 잊어버림(개발자 제외)
java.remove("김태호")
print(java)