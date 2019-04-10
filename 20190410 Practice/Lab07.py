# 20190410 Lab07
# 전역변수와 지역변수의 이해

def sub(x, y):
    global a

    a = 7
    x, y = y, x
    b = 3
    print(a, b, x, y)


a, b, x, y = 1, 2, 3, 4
sub(x, y)
print(a, b, x, y)
