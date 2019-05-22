# 20190522 Lab06
# 자연수 N을 입력 받은 다음, 1을 입력하면 1부터 N 이하의 홀수, 2를 입력하면 2부터 N 이하의 짝수를 출력하는 프로그램 작성

def while_odd(n):
    print('while로 구한 N의 홀수')
    i = 1
    while i <= n:
        if i % 2 == 1:
            print(i, end=' ')
        i += 1

def while_even(n):
    print('while로 구한 N의 짝수')
    i=1
    while i <= n:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1

def for_odd(n):
    print('\nfor로 구한 N의 홀수')
    for j in range(1, n + 1):
        if j % 2 == 1:
            print(j, end=' ')

def for_even(n):
    print('\nfor로 구한 N의 짝수')
    for j in range(1, n + 1):
        if j % 2 == 0:
            print(j, end=' ')


n = int(input('N = '))
choice = int(input('홀수/짝수 선택(1.홀수, 2.짝수): '))
if choice == 1:
    while_odd(n)
    for_odd(n)
elif choice == 2:
    while_even(n)
    for_even(n)



