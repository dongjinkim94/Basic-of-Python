# 20190417 Lab05
# 계산기 프로그램 만들기 (실습) (sh)
# 계산기 프로그램을 만들어보자. (실행은 0, 종료는 1)
# 실행, 종료 결정 시 다른 문자가 들어가도 종료가 되지 않게 한다.
# +,-,*,/ 연산이 가능하게 프로그램 만들기
# 다른 문자가 들어가면 실행이 되지 않는다.

while True:
    print("========================================")
    print("계산기 프로그램 만들기")
    print("0. 계산기 실행하기")
    print("1. 종료하기")
    print("========================================")
    executeCode = int(input("실행 : "))
    if (executeCode == 1):
        print("프로그램 종료")
        break
    firstNumber = int(input("첫번째 수를 입력해주세요 : "))
    operator = input("계산 연산자를 입력해주세요(+,-,*,/) : ")
    secondNumber = int(input("두번째 수를 입력해주세요 : "))

    if (operator == '+'):
        print("더하기 결과는", firstNumber + secondNumber, "입니다.")
    elif (operator == '-'):
        print("빼기 결과는", firstNumber - secondNumber, "입니다.")
    elif (operator == '*'):
        print("곱하기 결과는", firstNumber * secondNumber, "입니다.")
    elif (operator == '/'):
        print("나누기 결과는", firstNumber / secondNumber, "입니다.")
    else:
        print("연산자 입력이 잘못되었습니다.")
