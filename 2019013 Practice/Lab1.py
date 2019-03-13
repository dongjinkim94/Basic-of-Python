# 20190313 프로그래밍 입문
# 숫자게임

a = 42
b = 0
print("숫자게임에 오신 것을 환영합니다.")

while a != b:
    b = int(input("1부터 100 사이의 숫자를 추측해보세요: "))
    if (a == b):
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
print("게임이 종료되었습니다.")

# hello
#
