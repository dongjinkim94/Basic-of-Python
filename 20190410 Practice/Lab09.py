# 20190410 Lab09
# 상수
# 파이를 전역 변수로 선언하고 이것을 이용하여서 원의 면적과 원의 둘레를
# 계산하는 함수를 작성해보자.

PI = 3.141592

def getArea(rad):
    Area = PI * rad **2
    return Area

def getRound(rad):
    Round = 2 * rad * PI
    return Round


radious = int(input("원의 반지름을 입력하시오: "))
print("원의 면적:",getArea(radious))
print("원의 둘레:",getRound(radious))


