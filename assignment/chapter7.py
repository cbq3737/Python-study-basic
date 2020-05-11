
#################################8번 ###############################################
# from StopWatch import *
#
# t = StopWatch()
#
# t.Start()
#
# sum = 0
# for i in range(0,1000001):
#     sum += i
#
# t.Stop()
#
# print(t.getElapsedTime())
#



#############################6번####################################################
# from Equation import *
# ## a,b,c = 1.0, 3, 1이면 두해  a,b,c = 1,2.0 ,1 이면 -1  a,b,c = 1,2,3이면 실근존재 x
# data =  QuadraticEquation(1,2,3)
#
# if data.getDiscriminant() > 0 :
#     print(data.getRoot1(),data.getRoot2())
# elif data.getDiscriminant() == 0 :
#     print(data.getRoot1())
# else :
#     print("이 방정식은 해가 없습니다.")

############################3번#####################################################
# from Account import *
#
# c = Accout(1122,20000000,4.5)
# print(c.getInfo())
#
# c.withdraw(2500000)
# print(c.getInfo())
#
# c.deposit(3000000)
# print(c.getInfo())

#############################1번########################################################
# from Rectangle import *
#
# r1 = Rectangle(4,10)
# r2 = Rectangle(3.5,35.7)
#
#
# print("폭,높이 : ",r1.getwidhei(),"넓이 :" , r1.getArea() , "둘레 :" ,r1.getPerimeter() )
# print("폭,높이 : ",r2.getwidhei(),"넓이 :" , r2.getArea() , "둘레 :" ,r2.getPerimeter() )
