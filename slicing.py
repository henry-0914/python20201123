rnumber = "991010-1234567"
print("sex : " + rnumber[7])
print("birth : " + rnumber[0:2]) # 0~ 2직전 즉 0.1번까지 가져옴
print("month : " + rnumber[2:4])
print("date : "  + rnumber[4:6])

print("birthday : " + rnumber[0:6])
print("birthday : " + rnumber[:6]) # 0을 제외해도 같은 값

print("back number : " + rnumber[7:14])
print("back number : " + rnumber[7:]) # 마지막 자리 안 써도 동일한 값

print("back number2 : " + rnumber[-7:])
# 맨 뒤 7번째부터 끝까지 