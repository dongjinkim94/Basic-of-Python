# 20190410 Lab10
# Line
# 2차원 평면에서 2개의 점을 입력 받았을 때,
# 2점을 지나는 직선의 기울기와 y절편을 반환하는 함수를 작성하시오

def get_line(x1,y1,x2,y2):
    if(x1 == x2):
        return 0, 0
    else:
        slope = (float)(y2-y1)/(x2-x1)
        yintercept = y1 - slope * x1
        return slope, yintercept

x1 = int(input("x1="))
# 작성중...