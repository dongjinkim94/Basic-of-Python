# 20190327 Lab 1
# 이차 방정식은 추억의 방정식일 것이다. 고등학교에서 아마 가장 중점적으로 학습한 내용이 아닐까 생각된다.
# 이차 방정식 aX^2 + bX + c = 0 의 근을 계산하는 프로그램을 작성하여 보자.

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

determine = (b ** 2) - (4 * a * c)
if a == 0 and b != 0:
    x = -c / b
    print("x = %.2f" % x)
elif a == 0 and b == 0:
    print("근이 없습니다.")
else:
    if determine == 0:
        x = (-b + determine ** 0.5) / (2 * a)
        print("x = %.2f" % x)
    elif determine > 0:
        x1 = (-b + determine ** 0.5) / (2 * a)
        x2 = (-b - determine ** 0.5) / (2 * a)
        print("x1 = %.2f" % x1)
        print("x2 = %.2f" % x2)
    else:
        print("근이 없습니다.")
