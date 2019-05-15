# 20190515 Lab06
# 문자열 분석
# 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을 작성하여 보자.
# string.isalpha() : 문자 여부 확인
# string.isdigit() : 숫자 여부 확인
# string.isspace() : 공백 여부 확인

text = input("문자열을 입력하시오: ")
dididic = {}
dididic['digits'] = 0
dididic['spaces'] = 0
dididic['alpas'] = 0

for words in text:
    if words.isalpha():
        dididic['alpas'] += 1
    elif words.isdigit():
        dididic['digits'] += 1
    elif words.isspace():
        dididic['spaces'] += 1

print(dididic)

