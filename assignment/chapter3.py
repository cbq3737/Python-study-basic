###################8번############################
# name = input("사원 이름을 입력하시오: ")
# weektime = eval(input("주당 근무시간을 입력하시오: "))
# money = eval(input("시간당 급여를 입력하시오: "))
# pay = eval(input("원천 징수 세율을 입력하시오: "))
# localpay = eval(input("지방세율을 입력하시오: "))
#
#
# total_money = money*weektime
# paypay = total_money*pay
# personpay = total_money*localpay
# total_pay = personpay+paypay
# last_money = total_money-total_pay
#
# print("사원이름: ", name)
# print("주당 근무시간: ", weektime)
# print("임금: ",money)
# print("총 급여: ",total_money)
# print("공제: \n","원천 징수세(",pay*100,"%): ",paypay)
# print("주민세(",localpay*100,"%): ",personpay)
# print("총공제: ",total_pay)
# print("공제 후 급여: ",last_money)

############################10번##########################https://blog.naver.com/13outsider/221289192427
#
# number= eval(input("정수를 입력하세요: "))
#
# print("숫자 역순은 ",str(number)[::-1],"입니다.") ##숫자 같은 경우 배열이 아니기 때문에 문자열로 변경하고 거꾸로 만든 다음 다시 숫자로 변환하는 과정을 거침

#############################14번############################

import turtle

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(45,80)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-45,80)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-55,0)
turtle.pendown()
turtle.goto(0,-30)

turtle.penup()
turtle.goto(55,0)
turtle.pendown()
turtle.goto(0,-30)

turtle.penup()
turtle.goto(-40,10)
turtle.pendown()
turtle.right(60)
turtle.circle(45,steps=3)
