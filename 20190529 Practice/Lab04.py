# 20190529 Lab04
# 매개변수로 주어진 n이 m의 약수인지 여부를 판별하는 함수
# isDivision(m,n)을 사용하여 자연수 a의 모든 약수를 구하는 프로그램 작성

def isDivisor(m, n):
    if m % n == 0:
        return True
    else:
        return False

a = int(input("a = "))
for i in range(1,a+1):
    if isDivisor(a,i):
        print(i,end=" ")