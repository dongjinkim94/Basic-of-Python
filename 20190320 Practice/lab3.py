# 20190320
# 사용자로부터 명령어를 받아서 터틀을 제어해보자.
# 즉 사용자가 "left"를 입력하면 왼쪽으로 60도 만큼 회전하고 50 steps 만큼 전진하고
# 사용자가 "right"를 입력하면 오른쪽으로 60도 만큼 회전하고 50 steos 만큼 전진하는 프로그램을 만들어 보자.

import turtle

t = turtle.Pen()

while True:
    input_string = input("Please choose the direction[left / right]: ")
    if input_string == "left":
        t.right(60)
        t.forward(50)

    elif input_string == "right":
        t.left(60)
        t.forward(50)

    elif input_string == "stop":
        print("End")
        break
    else:
        print("Retype\n")
