# 20190424 Lab11
# 연락처 관리 프로그램
# 파이썬을 이용하여 연락처르 관리하는 프로그램을 작성하여 보자.
# 연락처 관리 프로그램은 다음과 같은 메뉴를 가져야 한다.



def basic():
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")

def func_1(friendsList):
    print(friendsList)

def func_2(friendsList):
    addName = input("이름을 입력하시오: ")
    friendsList.append(addName)

def func_3(friendsList):
    deleteName = input("이름을 입력하시오: ")
    if deleteName in friendsList:
        friendsList.remove(deleteName)
    else:
        print("이름이 발견되지 않았습니다.")
def func_4(friendsList):
    beforeChangeName = input("변경전 이름을 입력하시오: ")
    if beforeChangeName in friendsList:
        index = friendsList.index(beforeChangeName)
        afterChangeName = input("변경할 이름을 입력하시오: ")
        friendsList[index] = afterChangeName
    else:
        print("이름이 발견되지 않았습니다.")
friendsList = []

while True:
    basic()
    select = int(input("메뉴를 선택하시오: "))
    if select == 1:
        func_1(friendsList)
    elif select == 2:
        func_2(friendsList)
    elif select == 3:
        func_3(friendsList)
    elif select == 4:
        func_4(friendsList)
    elif select == 9:
        break
