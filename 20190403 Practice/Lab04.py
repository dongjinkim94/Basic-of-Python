# 20190403 Lab04
# 문자열 중에서 자음과 모음의 개수를 집계하는 프로그램 작성하여 보자.

original = input("문자열을 입력하시오:")
word = original.lower()
vowels = 0
consonants = 0

if len(original) > 0 and original.isalpha():
    for char in word:
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print("모음의 개수",vowels)
print("자음의 개수",consonants)
