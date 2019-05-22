# 20190522 Lab03
# 자연수 a를 입력 받아서 a의 모든 약수를 출력하는 프로그램을 작성하시오
#
# 입력: 자연수 a
# 출력: a의 모든 약수

target = int(input('자연수 하나를 입력하세요: '))
print('약수의 값: ')
for i in range(1,target+1):
    if target % i == 0:
        print(i,end=" ")

