# 20190522 Lab08
# 자연수가 아닌 수를 입력하면 자연수를 입력할 때까지 반복해서 데이터를 입력 받음

while True:
    target = int(input('자연수 하나를 입력하세요: '))

    if target > 0: break

    print(target, '은(는) 자연수가 아닙니다.')

print('약수의 값: ')
for i in range(1, target + 1):
    if target % i == 0:
        print(i, end=' ')