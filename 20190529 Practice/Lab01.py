# 20190529 Lab01
# 두 수를 입력받아 양,음수를 판별하는 문제

while True:
    a = int(input("a="))
    b = int(input("b="))

    if (a>0 and b>0) or (a<0 and b<0):
        print("양수")
    else:
        print("음수")