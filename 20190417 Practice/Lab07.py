# 20190417 Lab07
# 숫자맞추기 게임 ver2
# 이 예제는 프로그램이 가지고 있는 정수를 사용자가 알아맞추는 게임이다.
# 사용자가 답을 제시하면 프로그램은 자신이 저장한 정수와 비교하여 제시된 정수가 더 높은지 낮은지 만을 알려준다.
# 정수의 범위를 1부터 100까지로 한정하도록 하자.
# 몇번의 기회 만에 이 문제를 해결하는지 알아보자.

from random import randint
print("숫자 게임에 오신것을 환영합니다.")
count = 0
ans = randint(1,100)
while True:
    guess = int(input("숫자를 맞춰 보세요 : "))
    if(guess == ans):
        print("사용자가 이기셨습니다.")
        print(count,"번의 기회만에 이기셨군요")
        print("게임 종료")
        break
    elif(guess > ans):
        print("너무 큼!")
    else:
        print("너무 작음!")
    count += 1