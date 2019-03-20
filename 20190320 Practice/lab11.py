# 20190320
# 사과사기
# 예를 들어보자.
# 마트에서 사과가 신선하면 사과를 사기로 한다.
# 만약 사과가 개당 1000원 미만이면 10개를 산다.
# 하지만 사과가 개당 1000원 이상이면 5개만 산다.

apple_status = input("사과의 신선한가? [Y,N]: ")
apple_price = int(input("사과의 금액을 입력하시오: "))
if apple_status == 'Y' or 'y':
    if apple_price >= 1000:
        print("사과 5개를 산다.")
    else:
        print("사과 10개를 산다.")
elif apple_status == 'N' or 'n':
    print("안산다. 사과.")
