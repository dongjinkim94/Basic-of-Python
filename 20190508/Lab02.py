# 20190508 Lab2
# 함수의 튜플 반환 예제
# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성, 테스트해보자.
from math import pi


def function(x):
    return (x ** 2 * pi, 2 * x * pi)


rad = int(input("원의 반지름을 입력하시오: "))
(area, round) = function(rad)
print("원의 넓이는", area, "이고 원의 둘레는", round, "이다.")
