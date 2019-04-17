# 20190417 Lab08
# 가위 바위 보
# 사용자가 가위, 바위, 보 중에서 하나를 선택하고 컴퓨터도 난수로 가위, 바위, 보 중에서 하나를 선택한다.
# 사용자의 선택과 컴퓨터의 선택을 비교하여서 승패를 화면에 출력한다.

from random import randint

random = randint(0,2)
if (random == 0):
    ans = "가위"
elif (random == 1):
    ans = "바위"
elif (random == 2):
    ans = "보"

guess = input("(가위,바위,보) 중에서 하나를 선택하세요 : ")
print("사용자",guess,"컴퓨터",ans)
if( guess == ans):
    print("비겼습니다.")
elif(guess == "가위" and ans == "바위"):
    print("컴퓨터가 이겼습니다.")
elif(guess == "가위" and ans == "보"):
    print("사용자가 이겼습니다.")
elif(guess == "바위" and ans == "보"):
    print("컴퓨터가 이겼습니다.")
elif(guess == "바위" and ans == "가위"):
    print("사용자가 이겼습니다.")
elif(guess == "보" and ans == "가위"):
    print("컴퓨터가 이겼습니다.")
elif(guess == "보" and ans == "바위"):
    print("사용자가 이겼습니다.")