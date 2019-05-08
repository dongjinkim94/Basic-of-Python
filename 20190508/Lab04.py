# 20190508 Lab4
# 파일에서 중복되지 않은 단어의 갯수
# 텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작성하였는지를 계산하는
# 프로그램을 작성해보자.

# 참고 -> 파일 Input, Output
# 파일을 연다.
# fname = input("입력 파일 이름: ") # Lab04_proverbs
# file = open(fname,"r") # r = read only, w = write
# 파일의 모든 줄에 대하여 반복한다.
# for line in file:
#   lineWords = line.split()

fname = input("입력 파일 이름: ")
file = open(fname, "r")  # r = read only, w = write
a = set([])
for line in file:
    # 단어 단위로 분리 -> 리스트 저장
    lineWords = line.split()

    # 리스트에 저장된 워드(단어)를 순차적으로 접근하면서 가져오는 것

    for words in lineWords:
        new_words = ""
        # 새로운 워드: 구두점(' or .) 등을 제거 순수 문자 저장
        # 문자 하나하나씩 접근
        for ch in words:
            # 알파벳(영문자) 저장
            if ch.isalpha():
                new_words += ch
        a.add(new_words.lower())
print(a)
print("%d개의 단어(중복제외)" % (len(a)))
