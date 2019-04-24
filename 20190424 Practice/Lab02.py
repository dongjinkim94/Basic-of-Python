# 20190424 Lab02
# 리스트에 값 집어넣기 2

scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

scores[0] = 80
scores[1] = scores[0]

i = 3
scores[i] = 10
scores[i + 2] = 20

number = 8
if i >= 0 and i < len(scores):
    scores[i] = number

print(scores)