# 20190320 lab2
# 눈이 올 때 어떻게 대처할 것인지를 순서도로 그려보라.
# 눈이 오지 않으면 외출한다. 눈이 오면 우산을 가지고 있는지 검사한다.
# 우산을 가지고 있다면 외출한다.
# 우산을 가지고 있지 않다면 무한정 눈이 그칠 때 까지 기다린다.

while True:
    qFirst = input("밖에 눈이 오나요? [Y/N]: ")
    if qFirst == 'Y' or qFirst == 'y':
        qSecond = input("우산을 가지고 있나요? [Y/N] : ")
        if qSecond == 'Y' or qSecond == 'y':
            print("밖으로 나갑니다.")
            break
        elif qSecond == 'N' or qSecond == 'n':
            print("밖으로 나가지 않습니다. 눈이 그칠 때까지 대기합니다.\n")
            break
        else:
            print("다시 입력해주세요!")
            break
    elif qFirst == 'N' or qFirst == 'n':
        print("밖으로 나갑니다.")
        break
    else:
        print("다시 입력해 주세요.")
