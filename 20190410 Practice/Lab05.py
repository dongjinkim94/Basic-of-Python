# 20190410 Lab05
# 구의 부피 계산
# 구의 부피를 계산하는 함수 sphereVolume()을 작성하여 보자.
# 반지름이 r인 구의 부피는 다음과 같다.

from math import pi


def sphereVolume(radious):
    volume = 4.0 / 3.0 * pi * radious ** 3
    return volume


radious = float(input("구의 반지름을 입력하시오: "))
print(sphereVolume(radious))
