###############################6번#####################
# number = eval(input("0과 1000사이의 숫자를 입력하세요: "))
# adder= number % 10 + (number // 10) % 10 + number // 100
# print("각 자릿수의 합은 : ", adder)


##########################14번#########################
# x1,y1 = eval (input("x1,y1의 좌표를 입력하시오 : "))
# x2,y2 = eval (input("x2,y2의 좌표를 입력하시오 : "))
# x3,y3 = eval (input("x3,y3의 좌표를 입력하시오 : "))
#
# ln1 = ((x2-x1)**2+(y2-y1)**2)**0.5
# ln2 = ((x3-x2)**2+(y3-y2)**2)**0.5
# ln3 = ((x1-x3)**2+(y1-y3)**2)**0.5
#
# s = (ln1+ln2+ln3)/2
#
# SS = (s*(s-ln1)*(s-ln2)*(s-ln3))**0.5
#
# print("삼각형의 넓이는 ", int(SS*10)/10 ,"입니다.")

########################26번#############################
# import turtle
# x1,y1,z = eval (input("원의 중점과 반지름 을 입력하시오.: "))
#
# circleS = z * z * 3.141592
#
# turtle.penup()
# turtle.goto(x1,y1)
# turtle.pendown()
#
# turtle.circle(z)
#
# turtle.penup()
# turtle.goto(x1,y1)
# turtle.write(int(circleS)*100/100)
#
# turtle.done()