# list[]
# 지하철 칸 별로 10, 20, 30명 

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석 조세호 사이에 태워 봄

subway.insert(1, "정형돈")
print(subway)

# 지하철에 타고 있는 사람을 뒤에서 부터 빼냄

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬 가능

num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 숫서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기 가능

num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [1,2,3,4,5]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)