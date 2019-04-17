# 20190417 Lab15
# 별찍기-4
# 별을 다음과 같이 찍어보자. (반복문, 조건문 사용 가능)

for i in range(1,10+1):
    for j in range(10,i,-1):
        print(" ",end="")
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, i):
        if j == 1:
            print("", end="")
        print("*", end="")
    print("")