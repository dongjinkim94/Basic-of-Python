# 20190417 Lab17
# 문자열 교차 결합
# 두 문자열이 주어졌을 때 두 문자열을 교차 결합하는 프로그램을 만들어보자.
# 두 문자열 중 가장 긴 문자열의 문자를 시작으로 번갈아 가면서 문자를 결합하면 된다.
# 예를 들어
# "ABCDEFG"와 "가나다"라는 문자열이 주어지면 프로그램은
# "A가B나C다DEFG"를 출력해야 한다.
# 단, 문자열을 결합하는 코드는 함수로 저의되어야 한다.

def CrossString(s1, s2):
    s1Len = len(s1)
    s2Len = len(s2)
    finish = min(s1Len, s2Len)
    for i in range(0, finish):
        print("%s%s" % (s1[i], s2[i]), end="")
    for i in range(finish, s1Len):
        print("%s" % s1[i], end="")

s1 = input("첫 번째 문자열 입력: ")
s2 = input("두 번째 문자열 입력: ")
CrossString(s1, s2)
# 두 문자열 길이의 차를 어떻게 처리하는지가 핵심
