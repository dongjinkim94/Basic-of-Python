# 20190410 Lab01
# 제곱을 반환하는 함수 만들기!

# 재귀함수 이용!
def power(target, square):
    if square != 0:
        return target * power(target, square - 1)
    else:
        return 1

# 일반적!
def powerpower(x,y):
    result = 1
    for i in range(y):
        result = result * x
    return result

print(power(5,3))
print(power(5,3))