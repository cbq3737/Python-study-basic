# ####################################13번 중복되는 애를 지우지말고 안되는 애를 리스트에 넣어라#################
# def elimiateDuplicates(arr):
#     lst=[]
#     for i in range(0,len(arr)-1):
#         if i==0 :
#             lst.append(arr[0])
#         for j in range(i+1,len(arr)):
#             while arr[i] != arr[j]:
#                 if arr[j] not in lst:
#                     lst.append(arr[j])
#                     if j < 9:
#                         j= j+1
#                     else :
#                         break
#                 else:
#                     break
#
#
#     return lst
#
# n = input("10개의 숫자를 입력하세요: ")
# arr =[]
# c = n.split()
# for i in range(len(c)):
#     arr.append(int(c[i]))
# print("중복을 제거한 고유한 숫자 : ",elimiateDuplicates(arr))
#

################################9번##################################################
# def deviation(arr):
#     dev = 0
#     cnt = 0
#     for i in range(int(len(arr))):
#         dev +=(arr[i]-mean(arr))**2
#         cnt += 1
#     deviation = (dev / (cnt -1))**0.5
#
#     return deviation
#
# def mean(arr):
#     avg =0
#     cnt =0
#     for i in range(int(len(arr))):
#         avg += arr[i]
#         cnt += 1
#     average = avg / cnt
#     return average
#
# n = input("숫자를 입력해주세요 : ")
# arr =[]
# c = n.split()
# for i in range(len(c)):
#     arr.append(float(c[i]))
#
# print("평균: ",mean(arr))
# print("표준편자: ",deviation(arr))

#################################스페이스를 구분으로 한줄에 받고 리스트에 넣는 방법#######################
# a = input("입력해주세요 : ")
# b =[]
# c = a.split()
# for i in range(len(c)):
#     b.append(int(c[i]))

############################1번#######################################################
# arr =[]
# for i in range(0,4):
#     arr.append(eval(input("점수를 입력하시오: ")))
#
#
# def score(arr):
#     if max(arr)-10 <= arr[i]:
#         return "A"
#     elif max(arr)-20 <= arr[i] and  arr[i] < max(arr)-10:
#         return "B"
#     elif max(arr)-30 <= arr[i] and arr[i] < max(arr)-20:
#         return "C"
#     elif max(arr)-40 <= arr[i] and arr[i] < max(arr)-30:
#         return "D"
#     else:
#         return "F"
# for i in range(0,4):
#     print("학생",i,"의 점수는 ",arr[i],"이고 성적은",score(arr),"입니다.")