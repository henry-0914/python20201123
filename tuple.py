# tuple은 list와 달리 내용 변경이나 추가가 어렵다. 그래서 속도가 리스트보다 빠르다

menu = ("돈까지", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 추가 생성이 안됨

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = ("김종국", 20, "코딩")
print(name, age, hobby)

