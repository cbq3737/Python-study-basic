##############################19번###############################
# value = eval(input("10진수의 값 입력: "))
# arr=[]
# def decimalToBinary(value):
#     if value == 1:
#         return arr.append(1)
#     else:
#         return decimalToBinary(value//2),arr.append(value % 2)
#
# decimalToBinary(value)
# print(arr)
######################6번##########################################3
# i = eval(input("Enter a i: "))
#
# def m(i):
#     if i == 1:
#         return 1 / 2
#     else:
#         return m(i-1)+ i / (i+1)
#
# print("m(i): ", m(i))

#####################3번, 유클리드알고리즘 ########################################3
# m = eval(input("m의 값을 입력하시오: "))
# n = eval(input("n의 값을 입력하시오: "))
#
# def gcd(m,n):
#     if m % n ==0:
#         return n
#     else:
#         return gcd(n,m%n)
#
# print(gcd(m,n))

###############################이진탐색##########################
# def recurSive(list,key):
#     low = 0
#     high = len(list)-1
#     return recurSivehelper(list,key,low,high)
#
# def recurSivehelper(list,key,low,high):
#     if low>high:
#         return False
#     mid = (low + high)//2
#     if key< list[mid]:
#         return recurSivehelper(list,key,low,mid-1)
#     elif key == list[mid]:
#         return mid
#     else:
#         return recurSivehelper(list,key,mid+1,high)
#
# def main():
#     list=[3,5,6,8,9,12,34,36]
#     print(recurSive(list,3))
#     print(recurSive(list,14))
# main()

#############################sort재귀함수
# def sort(lst):
#     sortHelper(lst,0,len(lst)-1)
# def sortHelper(lst,low,high):
#     if low < high:
#         indexMin = low
#         min = lst[low]
#         for i in range(low+1,high+1):
#             if lst[i] < min:
#                 min = lst[i]
#                 indexMin = i
#         lst[indexMin]= lst[low]
#         lst[low]= min
#         sortHelper(lst,low+1,high)
# 
# def main():
#     lst=[3,2,1,5,9,0]
#     sort(lst)
#     print(lst)
# main()
###################palindrome##############################
# def main():
#     s = input("Enter a string: ").strip()
#
#     if isPalindrome(s):
#         print(s,"is Palindrome")
#     else:
#         print(s,"is not a Palindrome")
#
# def isPalindrome(s):
#     return isPalindromeHelper(s,0,len(s)-1)
#
# def isPalindromeHelper(s,low,high):
#     if high<=low:
#         return False
#     elif s[low] != s[high]:
#         return False
#     else:
#         return isPalindromeHelper(s,low+1,high-1)
# main()
# def main():
#     s = input("Enter a word").strip()
#
#     if isPlindrome(s):
#         print(s,"is Palindrome")
#     else:
#         print(s,"is not a Palindrome")
#
# def isPlindrome(s):
#     low = 0
#     high = len(s)-1
#     while low < high:
#         if s[low] != s[high]:
#             return False
#         low +=1
#         high -=1
#     return True
# main()
##########################Fibonacci########################
# def main():
#     n = eval(input("fibonacci: "))
#     print("Fibonacci of", n,"is",Fibonacci(n))
# def Fibonacci(n):
#     if n ==0 :
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# main()
###############################factorial#################
# def main():
#     n = eval(input("Enter a nonnegative: "))
#     print("Factorial of",n, "is",factorial(n))
#
# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# main()