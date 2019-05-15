# 20190515 Lab04
# 회문 검사하기
# 회문은 앞으로 읽으나 뒤로 읽으나 동일한 문장이다.
# 예를 들어서 "mom","civic","dad" 등이 회문의 예이다.
# 사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하여 보자.

text = input("문자열을 입력하시오 : ")
flag = 0
length = len(text)
for i in range(length // 2):
    if (text[i] != text[length - 1 - i]):
        flag = 1
if (flag):
    print("회문 아니다")
else:
    print("회문")


#####################SOL#####################

def check_pal(s):
    low = 0
    high = len(s) - 1

    while True:
        if low > high:
            return True
        a = s[low]
        b = s[high]

        if a != b:
            return False
        low += 1
        high -= 1


s = input("문자열을 입력하시오: ")
s = s.replace(' ', '')
if (check_pal(s) == True):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
