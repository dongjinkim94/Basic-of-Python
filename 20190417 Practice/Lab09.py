# 20190417 Lab09
# 문자열 조사
# 문자열을 조사하여서 알파벳 문자의 개수, 숫자의 개수, 스페이스의 개수를 출력하는 프로그램을 작성하라.

str = input("문자열을 입력하시오: ")
alphaCount =0
spaceCount = 0
numCount = 0

for char in str:
    if char.isalpha():
        alphaCount += 1
    if char.isnumeric():
        numCount += 1
    if char.isspace():
        spaceCount +=1

print("알파벳 문자의 개수 =",alphaCount)
print("숫자 문자의 개수 =",numCount)
print("스페이스 문자의 개수 =",spaceCount)