 #########################################################배열안에잇는원소찾기################
# def eliminateDuplicates(lst):
#     newList = []
#     for i in range(0,len(lst)):
#         checkNum = lst[i]
#         if not(checkNum in newList):
#             newList.append(checkNum)
#     return newList
#
# def countNumber(lst):
#     count = 0;
#     for i in range(1,101):
#         for j in range(0,len(lst)):
#             if(lst[j]==i):
#                 count = count+1
#         if (count>0):
#             print(i,"occurs",count,"time")
#         count =0
#
# def main():
#     num = input("Enter the integers between 1 and 100 :  ")
#     items = num.split()
#     numbers = [ eval(x) for x in items ]
#     countNumber(numbers)
#     NewList = eliminateDuplicates(numbers)
#     print("The distinct numbers ar :", end = " ")
#     print(NewList)
#
# main()

#######################주어진 배열과 타겟숫자가 주어지면,합이 타겟값이 되는 두원소의 인덱스를 찾으십시오.Java HashMap사용,풀지못함 #########################
import random

# def main():
#     arr= [2,5,6,1,10]
#     print("배열 : ", arr, end="")
#     target = eval(input("타켓값을 적으십시오: "))
#     print(Findidx(arr,target))
#
#
# def Findidx(arr,target):
#     arr2 = {}
#     for i in range(0,len(arr)):
#         remain = target - arr[i]
#         if remain in arr[0:]:
#             return arr2.get(remain),i
#         arr2[remain]=i
#
# main()

########################정수가 주어졌을 시,팰린드롬(앞에서부터 읽으나 뒤에서 읽으나 같은 수 ),단 정수를 문자열로 x##################
# arr =[]
# n = eval(input("정수를 적으시오: "))
# # 12321,-101,11111,12345
#
# def Solution(arr,n):
#     brun = 0
#     remain = n
#     while brun >= 0:
#         if remain < 0 or (remain % 10 ==0 and remain != 0) :
#             return False
#         if remain > 0 or remain // 10 > 0:
#             nn = remain % 10
#             arr.append(nn)
#             remain = remain // 10
#         if remain <= 0 :
#             for i in range(len(arr)//2):
#                if arr[i] == arr[len(arr)-1-i]:
#                    continue
#                else :
#                    return False
#             return True
#
# print(Solution(arr,n))


############정수 n이 주어지면 "(",")"으로 만들수있는 괄호조합을 모두 구하시오################재귀함수사용->해답보고 품
# def solution(n,open,close,bracket,arr):
#     if(close == n):
#         arr.append(bracket)
#         return
#     if  open< n:
#         solution(n,open+1,close,bracket+"(",arr)
#         print("+")
#
#     if close < open:
#         solution(n,open,close+1,bracket+")",arr)
#         print("-")
# arr = []
# n = eval(input("정수 n : "))
# solution(n,0,0,"",arr)
# print(arr)

############피보나치 배열은 0,1로 시작하며 주어진 정수 N보다 작은 짝수 피보나치의 합을 구하시오.############
# arr =[]
# N = eval(input("주어진 정수 N: "))
#
# def Fibo(N):
#     arr.append(0)
#     arr.append(1)
#     i=2
#     cnt = 0
#     while cnt < 1:
#         arr.append(arr[i-1]+arr[i-2])
#         if arr[i] > N:
#             cnt = cnt+1
#             arr.pop()
#         i = i + 1
#     return arr
#     NumSum(arr)
#
# def NumSum(arr):
#     sum = 0
#     for i in range(2,len(arr),1):
#         if arr[i] % 2 == 0:
#             sum += arr[i]
#     return sum
#
#
# print("N보다 작은 피보나치 수열은 : ",Fibo(N),"짝수의 합은: ",NumSum(arr))
#


############정수 배열이 주어지면 이어지는 원소의 합 중 가장큰 이어지는 합을 구하시오#################
# arr =[]
# def SumIndex(arr,n):
#     max = arr[0]
#     nn = -1
#     for i in range(0,n):
#         nn = nn + 1
#         sum = 0
#         for j in range(nn,n):
#             sum += arr[j]
#             if sum > max:
#                 max = sum
#     return max
#
# n = eval(input("배열의 크기를 입력하시오: "))
#
# for i in range(0,n):
#     idx = eval(input("원소의 값: "))
#     arr.append(idx)
#
# print(arr,"의 가장 큰 원소합은 ",SumIndex(arr,n),"입니다.")
#

##################임의의 정수 배열이 주어지고 임의의 정수 N번째로 큰 원소를 프린트하시오######################
# import random
#
# arr=[]
# n = random.randint(2,10)
#
# def SortArray(n):
#     for i in range(0,int((n-1)*n/2)):
#         for j in range(0,n-1):
#             if arr[j] < arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     print(arr)
#
# def PrintIndex(N):
#     SortArray(n)
#     return arr[(N-1)]
#
#
# for i in range(0,n):
#     r = random.randint(0,10)
#     arr.append(r)
# print(arr)
# N= eval(input("N번째로 큰 원소"))
#
# print(N,"번째로 큰수",PrintIndex(N))

########################정수배열과 정수N이 주어졌을때, 배열 안의 합이 N이 되는 두 수를 찾아라##########
# import random
#
# def calculate(integer):
#         for i in range(0,4):
#             for j in range(i+1,5):
#                 if arr[i]+arr[j] == integer :
#                     print("idx:",i,"번째",arr[i],'+',"idx",j,"번째",arr[j],'=',integer)
#             if arr[i] + arr[j] != integer:
#                 print("There no exist")
#
# arr=[]
# count =0
# integer = random.randint(0,10)
#
# while count < 5:
#     number = random.randint(0,10)
#     arr.append(number)
#     count += 1
# print(arr, integer)
#
# calculate(integer)

##############i=1,101,201,301...601까지#############################
# def mi(n):
#     sum = 0
#     for j in range(1,n+1):
#         sum += ((-1)**(j+1))/(2*j-1)
#     return (4*sum)
#
# def main():
#     for i in range(1,1000,100):
#         print("i","mi", i,format(mi(i),'5.4f'))
#
# main()
##################10진수 8진수################
# def main():
#     n1 = eval(input("10진수를 입력하시오:"))
#
#     print(pal(n1))
#
#
# def pal(sip):
#     result=''
#     while sip != 0:
#         remain=sip % 8
#         remain=chr(remain+ord('0'))
#         result=remain+result
#         sip=sip//8
#     return result
#
# main()
##############소tn 50개###########################
# def main():
#
#     n1 = 50
#     prim(n1)
#
# def prim(n2):
#     cnt=0
#     number = 2
#     while cnt < n2:
#         prime = True
#         divisor =2
#         while divisor <= number /2:
#             if number % divisor ==0:
#                 prime = False
#             divisor += 1
#         if prime:
#             cnt += 1
#             print(number, end=" ")
#
#         if cnt % 10 ==0:
#             print()
#         number += 1
#
# main()
###############소수 찾기###########################
# def main():
#
#     n1=eval(input("정수를 입력하시오: "))
#
#     print(n1,"까지의 소수")
#     prim(n1)
#
# def prim(n2):
#     cnt=0
#     for i in range(2,n2+1):
#
#         for j in range(2,i+1):
#             if j==i:
#                 cnt += 1
#                 print(format(j,"3d"),end=' ')
#             elif i%j==0:
#                 break
#         if cnt % 10 == 0:
#             print("")
#
# main()
###################심종현 중간고사 4번#######################
# def cal(n1,n2,yeon):
#     if yeon == '+':
#         return plus(n1, n2)
#     elif yeon == '-':
#         return min(n1, n2)
#     elif yeon == '*':
#         return mul(n1, n2)
#     elif yeon == '/':
#         return div(n1, n2)
#
#
# def plus(n1, n2):
#     return n1 + n2
#
#
# def min(n1, n2):
#     return n1 - n2
#
#
# def mul(n1, n2):
#     return n1 * n2
#
#
# def div(n1, n2):
#     return n1 / n2
#
# def main():
#     yeon = input("연산입력(+,-,*,/)")
#     n1 = eval(input("첫번째 숫자 입력"))
#     n2 = eval(input("두번째 숫자 입력"))
#
#     print("계산기: ",n1,yeon,n2,cal(n1,n2,yeon))
# main()
###################심종현 중간고사 3번########################
# import random
# for i in range(0,5):
#     number = random.randint(0,52)
#     print("랜덤숫자",number)
#     if number // 13 == 0:
#         print("스페이드",end ="")
#     elif number // 13 == 1:
#         print("하트",end ="")
#     elif number // 13 == 2:
#         print("클로버",end ="")
#     elif number // 13 == 3:
#         print("다이아몬드",end ="")
#
#     if number % 13 ==0:
#         print('A')
#     elif number % 13 ==10:
#         print('J')
#     elif number % 13 ==11:
#         print('Q')
#     elif number % 13 ==12 :
#         print('K')
#     else :
#         print(number % 13+1 ) #숫자카드엔 1이 없다.
#
###################엄영철 중간고사 2번########################
# day = 0
# 심종현 : month  = 0
# q = "1월  2월  3월  4월\n" + \
#     "5월  6월  7월  8월\n" + \
#     "9월 10월 11월 12월\n" + \
#     "당신의 생일이 포함한 월은? "
#
# a = input(q)
# print()
#
# question1 = "Set1에 당신의 생일이 있습니까?\n" + \
#             " 1 3 5 7\n" + \
#             " 9 11 13 15\n" + \
#             " 17 19 21 23\n" + \
#             " 25 27 29 31\n" + \
#             "아니오(0) 예(1)"
#
# answer = eval(input(question1))
# if answer == 1:
#     day += 1
# print()
#
# question2 = "Set2에 당신의 생일이 있습니까?\n" + \
#             " 2 3 6 7\n" + \
#             " 10 11 14 15\n" + \
#             " 18 19 22 23\n" + \
#             " 26 27 30 31\n" + \
#             "아니오(0) 예(1)"
#
# answer = eval(input(question2))
# if answer == 1:
#     day += 2
#
# question3 = "Set3에 당신의 생일이 있습니까?\n" + \
#             " 4 5 6 7\n" + \
#             " 12 13 14 15\n" + \
#             " 20 21 22 23\n" + \
#             " 28 29 30 31\n" + \
#             "아니오(0) 예(1)"
#
# answer = eval(input(question3))
# if answer == 1:
#     day += 4
#
# question4 = "Set4에 당신의 생일이 있습니까?\n" + \
#             " 8 9 10 11\n" + \
#             " 12 13 14 15\n" + \
#             " 24 25 26 27\n" + \
#             " 28 29 30 31\n" + \
#             "아니오(0) 예(1)"
#
# answer = eval(input(question4))
# if answer == 1:
#     day += 8
#
# question5 = "Set5에 당신의 생일이 있습니까?\n" + \
#             " 16 17 18 19\n" + \
#             " 20 21 22 23\n" + \
#             " 24 25 26 27\n" + \
#             " 28 29 30 31\n" + \
#             "아니오(0) 예(1)"
#
# answer = eval(input(question5))
# if answer == 1:
#     day += 16
#######month구하기
############################################
# question6 = "Set1에 당신의 생일중 월이 있습니까?\n" + \
#             " 1  3  5  7\n" + \
#             " 9 11      " + \
#             "\n0(아니오)또는 1(예)를 입력하시오.: "
# answer = eval(input(question6))
#
# if answer == 1:
#     month += 1
#
# question7 = "Set2에 당신의 생일중 월이 있습니까?\n" + \
#             " 2  3  6  7\n" + \
#             "10 11 " + \
#             "\n0(아니오)또는 1(예)를 입력하시오.: "
# answer = eval(input(question7))
#
# if answer == 1:
#     month += 2
#
# question8 = "Set3에 당신의 생일중 월이 있습니까?\n" + \
#             " 4  5  6  7\n" + \
#             "12 " + \
#             "\n0(아니오)또는 1(예)를 입력하시오.: "
# answer = eval(input(question8))
#
# if answer == 1:
#     month += 4
#
# question9 = "Set4에 당신의 생일중 월이 있습니까?\n" + \
#             " 8  9 10 11\n" + \
#             "12 " + \
#             "\n0(아니오)또는 1(예)를 입력하시오.: "
# answer = eval(input(question9))
#
# if answer == 1:
#     month += 8
# print("너의 생일은", str(a), day, "일!")

#############중간고사 엄영철 1번#################
# import turtle
#
# x1,y1= eval(input("x1,y1의 좌표입력: "))
# r1 = eval(input("첫 번째 원 반지름 입력: "))
# x2,y2 = eval(input("x2,y2의 좌표입력: "))
#
# d = ((x2-x1)**2+(y2-y1)**2)**0.5
#
# turtle.penup()
# turtle.goto(x1,y1-r1)
# turtle.down()
# turtle.circle(r1)
#
#
# turtle.penup()
# turtle.goto(x2,y2-3)
# turtle.down()
# turtle.begin_fill()
# turtle.color("red")
# turtle.circle(3)
#
# if d< r1:
#     turtle.write("The poin is inside the circle")
#     turtle.end_fill()
# elif d ==r1:
#     turtle.write("The point is on the Circle")
#     turtle.end_fill()
#
# elif d> r1:
#     turtle.write("The point is outside the Circle")
#     turtle.end_fill()
#
# turtle.done()

############직사각형 안에 랜덤으로 원을 그려라############3
# import turtle
# import random
# 
# turtle.penup()
# turtle.goto(0,50)
# turtle.pendown()
# turtle.forward(60)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(120)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(60)
# 
# number = random.randint(0,20)
# 
# for i in range(number):
#     width = random.randint(-117, 117)
#     height = random.randint(-97, 97)
#     turtle.penup()
#     turtle.goto(width/2,height/2)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.color("red")
#     turtle.circle(3)
#     turtle.end_fill()
# turtle.done()

##################등록금이 연 5%씩 인상된다고 할때, 10년간의 등록금과 , 4년간의 등록금의 합계를 현재부터 10년간############
# price = 1000000
# price2 = 1000000
# newprice = 0
# year = 2019
# for i in range(0,11):
#      price *= 1.05
# print("10년간 등록금",price)
#
# for j in range(0,8):
#     price3 = price2
#     for k in range(0,4):
#         if (k+1) % 5 != 0:
#             newprice += price3
#         price3 *= 1.05
#     price2 *= 1.05
#     print((year-1)+(j+1),"년부터",(year-1)+(j+4),"년까지 등록금은",newprice)
#     newprice =0

########################100이하의 정수를 2개 생성하고 합이 맞는지 맞추는 프로그램#####################
# import random
#
# rand1 = random.randint(0,100)
# rand2 = random.randint(0,100)
# run = 0;
# plus = rand1+rand2
#
# while(run==0):
#     x = eval(input("정수의 합을 예상해보시오: "))
#     if x == plus:
#         print("정답입니다. ",x)
#         run =1
#     elif x > plus:
#         print("더 작습니다. ")
#     else :
#         print("더 큽니다.")
###############행의 개수를 입력하고 숫자 피라미드를 만들어보시오.(왼쪽은 역, 오른쪽은 오름),파이썬 교재 5.19
# n = eval(input("행의 개수를 입력하시오: "))
# 
# for i in range (n):
#     for j in range((n-1)-i):
#         print(" ",end=" ")
#     for j in range((n+i)-(n-1),0,-1):
#         print(j,end=" ")
# 
#     for j in range((n+i)-n):
#         print(j+2,end=" ")
#     print()

###################길이가 N인 배열에 1부터 N까지 숫자가 중복없이 한번씩 들어있는지 확인하시오.######
# import random
# n = eval(input("배열의 길이를 입력하시오: "))
# arr=[]
#
# compare = int((n-1)*n/2)
#
# for i in range(n):
#     r = random.randint(0, 10)
#     arr.append(r)
#
# for i in range(compare):
#     for j in range(1,n-1):
#         if i < (j+1):
#             if arr[i] == arr[j+1]:
#                 print("중복되는 수",i,"번째",arr[i], (j+1),"번째", arr[j + 1], "가 있습니다.")



#########################정수배열과 정수k가 주어지면 모든 원소를 k칸씩 앞으로 옮기시오################################.
# n = eval(input("원하는 배열의 크기를 정하시오: "))
# k = eval(input("몇 칸을 움직일지 정하시오: "))
# arr = []
#
# for i in range(n):
#     arr.append(i)
#     print("할당된 배열: ",arr[i], end=" ")
# print()
#
# for i in range(k):
#     temp = arr[0]
#     for j in range(n-1):
#         arr[j]= arr[j+1]
#     arr[n-1]= temp
#
# for i in range(n):
#     print(k,"칸 움직인 배열: ",arr[i])
