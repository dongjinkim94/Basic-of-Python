# 20190417 Lab10
# 문자열 조사(아스키코드)
# 문자열을 조사하여서 아스키 코드값으로 비교하는 프로그램을 작성하라.

str = input("문자열을 입력하시오: ")
alphaCount =0
spaceCount = 0
numCount = 0

for char in str:
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        alphaCount += 1
    if ord(char) >= 48 and ord(char) <= 57:
        numCount += 1
    if ord(char) == 32:
        spaceCount +=1

print("알파벳 문자의 개수 =",alphaCount)
print("숫자 문자의 개수 =",numCount)
print("스페이스 문자의 개수 =",spaceCount)