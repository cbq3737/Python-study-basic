#####################5번###########################################3
# s1 = input("문자열입력: ").strip()
# s2 = input("문자열 입력: ").strip()
#
# def count(s1,s2):
#     return s1.count(s2)
#
# print(count(s1,s2))
##################################11번 문자열 역순######################################
# s = input("문자열을 입력하시오: ")
#
# def reverse(s):
#     return s[::-1]
#
# print(reverse(s))
#


######################8번##############################################
# def main():
#     binaryString = input("2진법을 입력하시오: ") #진법이므로 정수형으로 받으면안됌.
#
#     decimal = binaryToDecimal(binaryString)
#
#     if decimal == None:
#         print("2진법이아닙니다.")
#     else :
#         print(decimal)
#
# def binaryToDecimal(binaryString):
#     Decimal = 0
#     for i in range(len(binaryString)):
#         ch = binaryString[i]
#         Decimal = Decimal * 2 + int(ch)
#     return Decimal
#
# main()

#####################4번###############################################
# str = input("문자열을 입력하시오: ").strip()
# n = input("찾고자하는 문자를 입력하시오: ")
# cnt = 0
# for i in range(len(str)):
#     if str[i] == n :
#         cnt += 1
# print(cnt)

######################16진법을 10진법으로, 하지만 변환하는 방식이 살짝 다름####################
# def main():
#     hex = input("Enter a hex number").strip()
#
#     decimal = hexToDecimal(hex.upper())
#
#     if decimal == None:
#         print("Incorrect hex number")
#     else :
#         print("The decimal value for hex number",hex,"is",decimal)
#
# def hexToDecimal(hex):
#     decimalValue = 0
#     for i in range(len(hex)):
#         ch = hex[i]
#         if 'A' <= ch <= 'F' or '0' <= ch <= '9':
#             decimalValue = decimalValue * 16 + hexCharToDecimal(ch)
#         else :
#             return None
#     return decimalValue
#
# def hexCharToDecimal(ch):
#     if 'A' <= ch  <= 'F':
#         return 10 + ord(ch) - ord('A')
#     else :
#         return ord(ch) - ord('0')
# main()