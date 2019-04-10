# 20190410 Lab04
# 소수 찾기
# 여기서는 소수를 판별하는 함수 is_prime()을 작성하여 사용하여 보자.

def is_prime(target):
    if target != 2 and target % 2 == 0:
        return False
    elif(target == 2):
        return True
    else:
        for i in range(3,target):
            if target % i == 0:
                return False
        return True

def is_prime2(target):
    for i in range(2, target):
        if(target%i == 0):
            return False
    return True

target = int(input("정수를 입력하세요: "))
print(is_prime(target))

target = int(input("정수를 입력하세요: "))
print(is_prime2(target))