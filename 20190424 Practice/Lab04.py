# 20190424 Lab04
# 문자열 처리 프로그램
# 리스트는 문자열도 저장할 수 있다. 강아지르 많이 키우는 사람을 가정하자.
# 강아지들의 이름을 저장하였다가 출력하는 프로그램을 작성해보자.(엔터키 문자열: "")
import string

dogs = []
while True:
    nameOfDog = input("강아지의 이름을 입력하시오(종료시에는 엔터키) ")
    if nameOfDog == "":
        break;
    else:
        dogs.append(nameOfDog)
print("강아지들의 이름:")
for name in dogs:
    print(name, end=", ")
