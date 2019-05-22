# 20190522 Lab05
# 자연수 N을 입력 받은 다음, N 이하의 홀수를 출력하는 프로그램을 작성하여 보자

n = int(input('N = '))
i = 1

print('while로 구한 N의 홀수')
while i <= n:
    if i % 2 == 1:
        print(i, end=' ')
    i += 1

print('\nfor로 구한 N의 홀수')
for j in range(1, n + 1):
    if j % 2 == 1:
        print(j, end=' ')
