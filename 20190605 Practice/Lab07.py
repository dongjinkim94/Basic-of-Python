# 20190605 Lab07
# 자연수 N과 m을 입력 받은 다음, N 이하의 m의 배수를 출력하는 프로그램을 작성
# for 문에서 사용하는 range() 함수의 매개변수를 통해 증가치를 설정

N = int(input("N = "))
m = int(input("m = "))

for i in range(0, N+1, m):
    if i > 0:
        print(i, end=" ")