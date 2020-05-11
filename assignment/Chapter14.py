####################################2번##########################################
# n = input("숫자 입력하시오: ")
# arr=[]
# dict= {}
# c = n.split()
# cnt = 0
# for i in range(len(c)):
#         arr.append(int(c[i]))
#         dict[int(c[i])]= cnt
#
# aset = set(arr)
# lst = list(aset)
#
# for i in range(len(lst)):
#     for j in range(len(arr)):
#         if lst[i] == arr[j]:
#             dict[lst[i]] +=1
# print(dict)
#
# reverse = [(value,key) for key,value in dict.items()]
#
# print(max(reverse))
#
# # aset = set(dict.keys())
# # lst = list(aset)
# #
# # for i in range(len(lst)):
# #     for key in arr:
# #         if arr[lst[i]]==key and arr[lst[i]] in arr:
# #             arr[lst[i]] += 1
# #
# # tuple1 = tuple(arr.values())
# # print(tuple1)
#########################################list,set 속도 비교################################
# import random
# import time
#
# Elements = 1000
#
# lst = [x for x in range(Elements)]
# random.shuffle(lst)
#
# s = set(lst)
#
# startTime = time.time()
# for i in range(Elements):
#     i in s
# endTime = time.time()
# runTime = int((endTime-startTime)*1000)
# print("To test if",Elements,"elements are in the set\n","The runtime is",runTime,"milliseconds")
#
# startTime = time.time()
# for i in range(Elements):
#     i in lst
# endTime = time.time()
# runTime = int((endTime-startTime)*1000)
# print("To test if",Elements,"elements are in the list\n","The runtime is",runTime,"milliseconds")
#
# startTime = time.time()
# for i in range(Elements):
#     s.remove(i)
# endTime = time.time()
# runTime = int((endTime-startTime)*1000)
# print("To test if",Elements,"elements are in the set\n","The runtime is",runTime,"milliseconds")
#
# startTime = time.time()
# for i in range(Elements):
#     lst.remove(i)
# endTime = time.time()
# runTime = int((endTime-startTime)*1000)
# print("To test if",Elements,"elements are in the list\n","The runtime is",runTime,"milliseconds")
