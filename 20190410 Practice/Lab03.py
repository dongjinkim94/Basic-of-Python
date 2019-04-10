# 20190410 Lab03
# 온도 변환 함수
# 섭씨 온도를 화씨 온도로 변환하여 반환하는 함수 fToC()를 작성하고 테스트하라.
# (C=(F-32)X5/9

def FtoC():
    felenhate = int(input("화씨온도를 입력하시오: "))
    celcious = (felenhate - 32) * 5 / 9
    return print(celcious)

def FtoC2(temp_f):
    temp_c = (5.0 * (temp_f - 32.0)) / 9.0
    return temp_c

FtoC()

temp_f = float(input("화씨온도를 입력하시오: "))

# FtoC2 함수 출력
print(FtoC2(temp_f))
