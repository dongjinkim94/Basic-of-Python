# 20190424 Lab14
# 주사위의 합 프로그램
# 2개의 주사위를 굴리면 다음 표와 같이 36가지의 결과가 나온다.
# 이것을 6X6 크기의 2차원 리스트로 생성하여 보자.
# (즉, 두 주사위값의 합이 2차원 리스트의 요소)

from random import random

rows = 6
cols = 6
table = []

# 2차원 리스트를 생성한다.
for row in range(rows):
    table += [[0] * cols]

# 2차원 리스트의 각 요소에 rows와 cols 값을 더하여 저장한다.
for row in range(rows):
    for col in range(cols):
        table[row][col] = (row + 1 + col + 1)

print(table)
