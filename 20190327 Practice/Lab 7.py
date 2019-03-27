# 20190327 Lab 7
# 화면에 사각형 그리기

import turtle

star = turtle.Turtle()

star.left(180)

for i in range(3):
    star.right(20)
    for i in range(4):
        star.forward(50)
        star.right(90)
