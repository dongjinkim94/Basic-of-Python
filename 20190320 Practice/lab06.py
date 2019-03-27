# 20190320
# 큰 수 찾기
# 사용자로부터 두개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램을 작성하여 보자.

firstInteger = input("첫번째 정수: ")
secondInteger = input("두번째 정수: ")
if firstInteger > secondInteger:  # String 끼리 숫자비교도 된다 ;;;;;;;;;;;;;;;;
    big = firstInteger
else:
    big = secondInteger
print("더 큰 수는 " + big)
