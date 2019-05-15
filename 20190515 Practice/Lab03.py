# 20190515 Lab03
# 축약어 풀어쓰기
# 현대인들은 축약어를 많이 사용한다. 예를 들어서 "B4(before)" "TX(Thanks)" "BBL(Be Back Later)" "BCNU(Be Seeing You)"
# "HAND(Have A Nice Day)"와 같은 축약어 들이 있다.
# 축약어를 풀어서 일반적인 문장으로 변환하는 프로그램을 작성하여 보자.
dddict = dict()
dddict['B4'] = 'Before'
dddict['TX'] = 'Thanks'
dddict['BBL'] = 'Be Back Later'
dddict['BCNU'] = 'Be Seeing You'

text = input("번역할 문장을 입력하시오: ")
newText = ''
for words in text.split():
    if words in dddict:
        newText += dddict.get(words)
    else:
        newText += words
    newText += ' '

print(newText)