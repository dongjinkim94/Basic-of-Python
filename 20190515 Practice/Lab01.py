# 20190515 Lab01
# 영한 사전 만들기
# 영한 사전을 구현하고자 한다. 어떻게 하면 좋은가?
# 공백 딕셔너리를 생성하고 여기에 영어 단어를 키로하고 설명을 값으로 하여 저장하면 될 것이다.. (one, two, three)

###########sol###########
english_dict = dict();  # 혹은 english_dict = {}
english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

word = input("단어를 입력하시오: ")
print(english_dict.get(word, "없음"))
