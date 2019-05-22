# 20190522 Lab07
# 자연수 N의 약수 출력하기, 자연수가 아닌경우 걸러내

target = int(input('자연수 하나를 입력하세요: '))

if target <= 0:
    print(target, '은(는) 자연수가 아닙니다.')
else:
    print('약수의 값: ')
    for i in range(1, target + 1):
        if target % i == 0:
            print(i, end=" ")
