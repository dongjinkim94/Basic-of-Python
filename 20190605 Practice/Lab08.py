# 20190605 Lab08
# 1부터 N^2 까지의 합을 구하는 프로그램의 실행시간 측정

import time

N = int(input("자연수 N 입력 : "))
sum = 0
start = time.time()
for i in range(1,N*N+1):
    sum += i
end = time.time() - start
print("합계 :",sum)
print("실행시간 :",end)