# 20190320
# 짐의 무게

weightString = input("짐의 무게는 얼마입니까? ")
weight = int(weightString)
if weight < 20:
    print("짐에 대한 수수료는 없습니다.\n감사합니다.")
else:
    print("무거운 짐은 20,000원을 내셔야 합니다.\n감사합니다.")
