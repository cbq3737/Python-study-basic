# ######################1번#############################
# a,b,c = eval(input("a,b,c의 값을 입력하시오: "))
#
# p= b**2-4*a*c
# r1 = (-b+p**0.5)/2*a
# r2= (-b-p**0.5)/2*a
#
# if p > 0:
#     print("실근은 ",format(r1,'10.6f'),"이고 ",format(r2,'10.6f'),"입니다")
# elif p == 0:
#     print("실근은 ",r2,"입니다.")
# else :
#     print("이방정식은 실근이 존재하지 않습니다.")
#####################21번#############################
# import turtle
#
# x1,y1 = eval(input("x,y의 좌표를 입력하시오: "))
#
# dist = (x1**2+y1**2)**0.5
#
# turtle.penup()
# turtle.goto(0,-10)
# turtle.pendown()
# turtle.circle(10)
#
# turtle.penup()
# turtle.goto(x1,y1)
# turtle.pendown()
# turtle.begin_fill()
# turtle.color("red")
# turtle.circle(2)
# turtle.end_fill()
#
# if dist <= 10:
#     print("점 x,y는 원의 내부에 있습니다.")
# else :
#     print("점 x,y는 원의 외부에 있습니다.")
######################39번#########################
import turtle

x1,y1,r1 = eval(input("원1의 좌표와 반지름을 입력하시오: "))
x2,y2,r2 = eval(input("원2의 좌표와 반지름을 입력하시오: "))


dist = ((x1-y1)**2+(x2-y2)**2)**0.5

turtle.penup()
turtle.goto(x1,y1-r1)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(x2,y2-r2)
turtle.pendown()
turtle.circle(r2)

if abs(r1-r2) < dist and r1+r2> dist:
    turtle.write("원1과 원2는 겹칩니다.")
elif r1+r2 < dist:
    turtle.write("원1과 원2는 겹치지 않습니다.")
elif r1-r2> dist :
    turtle.write("원2는 원1안에 있습니다.")

turtle.done()