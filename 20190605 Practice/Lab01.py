# 20190605 Lab01
# 두 수의 최대공약수를 구하는 알고리즘

print("자연수 a와 b를 입력하세요.")
a = int(input("a = "))
b = int(input("b = "))

i=1
while(i<= a and i<= b):
    if(a % i == 0 and b % i == 0):
        gcd = i
    i += 1

print("GCD의 값",gcd)