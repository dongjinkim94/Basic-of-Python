# 20190417 Lab06
# 이 예제는 프로그램이 가지고 있는 정수를 사용자가 알아맞추는 게임이다.
# 사용자가 답을 제시하면 프로그램은 자신이 저장한 정수와 비교하여 제시된 정수가 더 높은지 낮은지만을 알려준다.
# 정수의 범위를 1부터 100까지로 한정하도록 하자.
# 그리고 사용자는 단 한 번의 기회만 가진다.

from random import randint
print("숫자 게임에 오신것을 환영합니다.")
guess = int(input("숫자를 맞춰 보세요 : "))
ans = randint(1,100)
if(guess == ans):
    print("맞았음")
elif(guess > ans):
    print("너무 큼!")
else:
    print("너무 작음!")
print("게임 종료")