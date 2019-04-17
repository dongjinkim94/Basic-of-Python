# 20190417 Lab03
# 거스름돈
# 상점 주인 A씨는 손님을 위해 거스름돈을 최소의 지폐와 동전으로 주려한다.
# A씨는 이를 자동으로 계산해주는 프로그램을 필요로 한다.
# A씨를 위해 물건값과 손님이 지불한 돈이 입력되었을 때.
# 만원, 오천원, 천원, 오백원, 오십원, 십원, 일원 단위로 각각 얼마나 손님에게 주어야 하는지 출력해주는 프로그램을 작성해보자.
# 단, 손님이 물건 값 보다 적은 돈을 지불하였을 경우 프로그램은 종료되어야한다.
# 힌트: 프로그램 종료는 exit(1)이란 코드로 수행할 수 있다.

productPrice = int(input("물건값을 입력하시오: "))
myMoney = int(input("지불할 금액을 입력하세요: "))
change = myMoney - productPrice

print("거스름돈: ", change,"원")
print("만원: ", change // 10000,"장")
change %= 10000
print("천원: ", change // 1000,"장")
change %= 1000
print("백원: ", change // 100,"개")
change %= 100
print("십원: ", change // 10,"개")
change %= 10
print("일원: ", change // 1,"개")
change %= 1








