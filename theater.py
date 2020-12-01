# import Exmodule
# Exmodule.price(3) # 3명이서 영화 보러 갔을 때 가격
# Exmodule.price_morning(4) #4명에서 조조 할인 영화 보러 갔을 때
# Exmodule.price_soldier(5) #5명에서 군인 할인 영화 보러 갔을 때

# import Exmodule as mv # mv란 가명을 사용해서 호출하는 방법

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from Exmodule import * # 그냥 모듈에 있는 것 모두 사용 가능

# price(3)
# price_morning(4)
# price_soldier(5)

# from Exmodule import price, price_morning # 군인 정보 필요 없을 시 사용
# price(5)
# price_morning(6)

from Exmodule import price_soldier as sol # 군인 가격만 필요하여 가명을 붙여서 사용
sol(5)
