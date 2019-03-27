# 20190313 프로그래밍 입문
# 구의 부피 계산하기
# 반지름이 r인 구의 부피는 다음과 같은 식으로 계산할 수 있다.
# 4/3 * PI * r^3
# 반지름이 5인 구의 부피를 계산하는 파이썬 프로그램을 작성해보자.

from math import pi

radius = 5
volumeOfSphere = 4 / 3 * pi * radius ** 3
print("반지름", radius, "인", "구의 부피 값: ", int(volumeOfSphere))
