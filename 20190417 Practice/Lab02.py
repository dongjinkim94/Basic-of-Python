# 20190417 Lab02
# 대화하는 프로그램 만들기 (실습)
# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자.
# 사용자는 1000원 짜리 지폐와 500원 짜리 동전, 100원 짜리 동전을 사용할 수 이싿.
# 물건값을 입력하고 1000원권, 500원짜리 동전. 100원짜리 동전의 개수를 입력하면 거스름돈을 계산하여서 동전으로 반환한다.

productPrice = int(input("물건값을 입력하시오: "))
bill = int(input("1000원 지폐 갯수: "))
coin500 = int(input("500원 동전 갯수: "))
coin100 = int(input("100원 동전 갯수: "))
change = bill * 1000 + coin500 * 500 + coin100 * 100 - productPrice
coin500 = change // 500
coin100 = (change - coin500 * 500) // 100
coin10 = (change - coin500 * 500 - coin100 * 100) // 10
coin1 = (change - coin500 * 500 - coin100 * 100 - coin10 * 10) // 1
print("500원 지폐갯수: ", coin500)
print("100원 동전갯수: ", coin100)
print("10원 동전갯수: ",coin10)
print("1원 동전갯수: ",coin1)

