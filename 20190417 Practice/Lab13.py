# 20190417 Lab13
# 별찍기-2
# 별을 다음과 같이 찍어보자. (반복문, 조건문 사용 가능)

for i in range(10,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("")