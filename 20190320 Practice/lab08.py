# 20190320
# 문자열의 중간문자
# 문자열의 중앙에 있는 문자를 출력한다. 예를 들어서 문자열이 "weekday"이라면 중앙의 문자는 "k"가 된다.
# 하지만 만약 문자열이 짝수개의 문자를 가지고 있다면 중앙의 2개의 글자를 출력한다.
# 예를 들어서 "string" 문자열에서는 "ri"를 반환한다.

str1 = input("문자열을 입력하시오: ")
str1_length = len(str1)
if (str1_length % 2) == 0:
    print("중앙글자는 " + str1[(str1_length // 2) - 1] + str1[str1_length // 2])
else:
    print("중앙글자는 " + str1[(str1_length + 1) // 2])
