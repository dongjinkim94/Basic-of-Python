# 20190327 Lab 14
# 자리수의 합
# 정수 안의 각 자리수의 합을 계산하는 프로그램을 작성해보자.
# 예를 들어서 1234라면 (1+2+3+4)를 계산하는 것이다.

num = int(input("숫자를 입력하시오: "))
tmp = num
sum = 0
while 1:
    if num == 0:
        break
    tmp = num % 10
    sum += tmp
    num = (num - tmp) / 10
print(int(sum))
