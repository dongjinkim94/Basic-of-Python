# 20190327 Lab 11
# 팩토리얼 계산
# 팩토리얼을 계산하는 프로그램을 작성하여 보자.
# 펙토리얼은 ~~~~ 그냥 아까 for로 했던 팩토리얼 계산을 while로 해보자 ㅡㅡ

i = 1
factorial = 1
while i <= 10:
    factorial *= i
    i += 1
print("10!은 %d입니다." % factorial)
