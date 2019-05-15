# 20190515 Lab05
# 머리 글자어 만들기
# 머리 글자어는 NATO 처럼 각 단어의 첫글자를 모아서 만든 문자열이다.
# 사용자가 문장을 입력하면 해당되는 머리 글자어를 출력하는 프로그램을 작성하여 보자.

text = input("문자열을 입력하시오: ")
newText = ''
for words in text.upper().split():
    newText += words[0]

print(newText)