# 20190522 Lab02
# 네 수를 입력받아 오름차순으로 정력된 세 정수를 나타내는 문제

print('네 수의 정렬: 정수 a,b,c,d 입력')
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))

print('정렬 전: ', a, b, c, d)

if a > b:
    b, a = a, b

if b > c:
    c, b = b, c

if c > d:
    d, c = c, d

if a > b:
    b, a = a, b

if b > c:
    c, b = b, c

if a > b:
    b, a = a, b

print('정렬 후: ', a, b, c, d)
