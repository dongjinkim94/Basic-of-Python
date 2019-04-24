# 20190424 Lab10
# 피타고라스 삼각형
# 피타고라스의 정리를 만족하는 삼각형들을 모두 찾아보자.
# 삼각형 한 변의 길이는 1부터 30 이하이다.

new_list = []

for x in range(1, 30):
    for y in range(x, 30):
        for z in range(y, 30):
            if x ** 2 + y ** 2 == z ** 2:
                new_list.append((x, y, z))
print(new_list)

#################### 한줄로 표현하기 ####################
new_list = []
new_list = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x ** 2 + y ** 2 == z ** 2]
print(new_list)
