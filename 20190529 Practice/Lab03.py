# 20190529 Lab03
# 매개변수로 주어진 세 정수 x,y,z의 최대값을 찾아서 반환해 주는 함수
# max3(x,y,z)를 사용하여 입력된 세 정수 a,b,c의 최대값을 구하는 프로그램 작성

def max3(x,y,z):
    maxy = max(x,y)
    maxy = max(maxy,z)
    return maxy

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
maxval = max3(a,b,c)

print("최대값 :",maxval)


