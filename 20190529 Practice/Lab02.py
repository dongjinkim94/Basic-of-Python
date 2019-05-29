# 20190529 Lab02
# 2보다 큰 자연수 N을 입력 받아 2부터 N까지의 자연수 중에서 완전수를 출력하는 프로그램 작성

def isPergect(a):
    v = 0
    for i in range(1, a):
        if a % i == 0:
            v += i
    if v == a:
        return True
    else:
        return False

n = int(input("n="))
if n<2:
    print("다시 입력하세요")
else:
    if isPergect(n):
        print("완전수")
    else:
        print("완전수 아님")


