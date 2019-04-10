# 20190410 Lab06
# 온도변환기
# 섭씨 온도를 화씨 온도로, 또 그반대로 변환하는 프로그램을 작성하여 보자.

def FtoC():
    temp_f = int(input("화씨온도: "))
    temp_c = (5.0 * (temp_f - 32.0)) / 9.0
    return print("섭씨온도: ", temp_c)


def CtoF():
    temp_c = int(input("섭씨온도: "))
    temp_f = temp_c * 9 / 5 + 32
    return print("화씨온도: ", temp_f)


while True:
    btn = input("'c' 섭씨 온도에서 화씨 온도로 변환\n'f' 화씨 온도에서 섭씨 온도로 변환\n'q' 종료\n메뉴에서 선택하세요: ")
    if btn == 'c':
        CtoF()
    elif btn == 'f':
        FtoC()
    elif btn == 'q':
        break
    else:
        continue
