print(2**3) # 2를 3번 곱한 것 2^3 = 8
print(5%3)  # 5를 3으로 나눈 나머지 = 2
print(10%3) # 10을 3으로 나눈 나머지 = 1
print(5//3) # 5를 3으로 나눈 몫 = 1

print(3 == 3) # equal value
print(3 + 4 == 7) # True, False

print(1 !=3) # not equal
print(not(1 !=3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 5) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4 # 14
print(number)
number = number + 4 # 18
print(number)
number +=4 # 18
number *=4
print(number)
number /=4
print(number)
number -=4
print(number) 

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3,14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # down 4
print(ceil(3.14)) # up 4
print(sqrt(16)) # square root 4

