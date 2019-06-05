# 20190605 Lab05
#

def isPrime(m): # 원래 순서도 상의 코드
    i = 2
    isP = True
    while i<= x/2 and isP == True:
        if x % i == 0:
            isP = False
        i+=1
    if isP == True:
        return True
    else:
        return False

def isPrime(m): # isP없는 코드
    i = 2
    while i<= x/2:
        if x % i == 0:
            return False
        i+=1
    return True


a = 0
while(a<=2):
    a = int(input("2 이상의 자연수 입력: "))
    if a >= 2: break
    else:
        print(a,"은(는) 2 이상의 자연수가 아닙니다.");
isPrime(a)


#isPPAP = True
#i = 2
#
#while (isPPAP == True and i <= 2):
#    if (a % i == 0):
#        isPPAP = False
#    i+=1

