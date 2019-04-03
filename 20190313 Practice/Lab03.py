# 20190313 프로그래밍 입문
# 변수 x와 변수 y의 값을 서로 바꾸는 프로그램을 작성해보자.
# 다음과 같은 프로그램으로는 변수의 값을 교환할 수 없다. 왜 그럴까?
# 그리고 해결 방법은 무엇일까?

# 상황1
print("바뀌지 않는 경우")
x = 10
y = 20
print("변경전 x의 값: ", x, "변경전 y의 값 ", y)
x = y
y = x
print("변경후 x의 값: ", x, "변경후 y의 값 ", y)

# 상황2
print("\n바뀌는 경우(변수이용)")
x = 10
y = 20
print("변경전 x의 값: ", x, "변경전 y의 값 ", y)
temp = x
x = y
y = temp
print("변경후 x의 값: ", x, "변경후 y의 값 ", y)

# 상황3
print("\n바뀌는 경우(swap 이용)")
x = 10
y = 20
print("변경전 x의 값: ", x, "변경전 y의 값 ", y)
(y, x) = (x, y)
print("변경후 x의 값: ", x, "변경후 y의 값 ", y)