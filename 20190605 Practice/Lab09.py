# 20190605 Lab09
#

N = int(input("2 이상의 자연수 입력 : "))
while N <= 1:
    print("잘못입력하셨습니다.")
    N = int(input("2 이상의 자연수 입력 : "))

a = list();
i = 0

while i <= N:
    a.append(i)
    i += 1

a[1] = 0
i = 2

while i <= N / 2:
    j = 2
    while (i * j <= N):
        a[i * j] = 0
        j += 1
    i += 1

print("0이 아닌 a[i]의 값")
for i in range(1, N + 1):
    if a[i]:
        print(a[i], end=" ")
