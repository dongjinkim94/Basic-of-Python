# 20190605 Lab02
# 두 수의 최소공배수를 구하는 알고리즘

def lcm(m, n):
    x = m
    y = n
    while x != y:
        if x < y:
            x += m
        else:
            y += n
    return x


print("자연수 a와 b를 입력하세요.")
a = int(input("a = "))
b = int(input("b = "))

print("최소공배수 : ", lcm(a, b))
