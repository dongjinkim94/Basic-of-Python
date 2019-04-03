# 20190403 Lab01
# 사용자로부터 임의의 개수의 성적을 받아서 평균을 계산한 후에 출력하는 프로그램을 작성하여 보자.
# 센티널로는 음수의 값을 사용하자.

print("종료하려면 음수를 입력하시오")
count = 0
sum = 0
while True:
    x = int(input("성적을 입력하시오: "))
    if (x < 0):
        print("성적의 평균은 %f입니다." % (sum / count))
        break;
    sum += x
    count += 1

