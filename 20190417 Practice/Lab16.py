# 20190417 Lab16
# 정수를 문자열로
# 파이썬의 내장 함수 str()을 사용하지 않고, 정수를 문자열로 바꾸어주는 함수를 정의하고 아래와 같이 출력해보자.

def int2str(intString):
    count = 0
    temp = intString
    outputString = ""
    while temp > 0:
        count += 1
        temp /= 10
    for i in range(1,count+1):
        outputString = str(intString % 10) + outputString
        intString //= 10
    return outputString

input = int(input("정수 입력: "))
print("입력된 숫자:",input)
print("입력된 숫자의 형: ",type(input))
output = int2str(input)
print("변환된 숫자:",output)
print("변환된 숫자의 형: ",type(output))

###############################망한코드#########################재희꺼 참조###############

