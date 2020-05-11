#######################3번############################
# from problem3 import *
#
# number = eval(input("정수를 입력하시오: "))
#
# print(reverse(number),isPalindrome(number))

####################5번###############################
# def displatSortedNumbers(num1,num2,num3):
#     arr=[num1,num2,num3]
#
#     for i in range(3):
#         for j in range(2):
#             if arr[j]> arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
#
# def main():
#     num1,num2,num3 = eval(input("무작위로 번호를 적으시오: "))
#
#     print("정렬된 숫자는",displatSortedNumbers(num1,num2,num3),"입니다.")
#
# main()

######################14번#########################

def pi(i):
    m = 0
    for i in range(1,i+1):
        m += ((-1)**(i+1)/((2*i)-1))*4
    return m

def printtable(i):
    print("i\t\t\tm(i)\n")
    for i in range(5):
        print(i*100+1,"\t\t",int(pi(i*100+1)*10000)/10000,"\n")
def main():
    i=1
    printtable(i)

main()