# 20190320 lab5
# ?
# 키보드에서 입력받은 정수가 홀수인지 짝수인지를 말해주는 프로그램을 작성하여 보자.
# 홀수와 짝수는 어떻게 구별할 수 있는가?

question = input("정수를 입력하시오: ")
if (int(question) % 2) == 1:
    print("입력된 정수는 홀수입니다.")
else:
    print("입력된 정수는 짝수입니다.")