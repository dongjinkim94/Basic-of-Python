# 20190605 Lab03
# 자연수 a를 입력 받아서 완전수 인지를 구하는 알고리즘

def isPerfect(a):
    s = 0
    i = 1
    while(i<=a/2):
        if(a % i == 0):
            s += i
        i+=1

    if (s == a):
        print("a는 완전수입니다.")
    else:
        print("a는 완전수가 아닙니다.")

a = int(input("자연수 a를 입력하세요: "))

isPerfect(a)

