
#############################################################2번################
# def sumMajorDiagonal(m):
#         sum = 0
#         for i in range(0,len(matrix)):
#             for j in range(0,len(matrix[i])):
#                 if i == j :
#                     sum += matrix[i][j]
#
#         print("주대각선에 포함된 원소의 합계는 ",sum,"입니다.")
#
#
#
# matrix =[]
# for i in range(0,4):
#     matrix.append([])
#     for j in range(0,4):
#         value =eval(input("원소입력: "))
#         matrix[i].append(value)
# print(matrix)
#
# sumMajorDiagonal(matrix)
###############################################1번##################################
# def sumColumn(matrix,columnIndex):
#         for j in range(0,columnIndex):
#             sum =0
#             for i in range(0,len(matrix)):
#                 sum+= matrix[i][j]
#             print(j,"번 원소의 합은",sum,"입니다.")
# matrix =[]
# row = eval(input("row를 입력: "))
# col = eval(input("col를 입력: "))
#
# for i in range(0, row):
#     matrix.append([])
#     for j in range(0, col):
#         value = eval(input("원소를 입력하세요: "))
#         matrix[i].append(value)
# print(matrix)
#
# sumColumn(matrix,col)
###################################스도쿠######################################
# from CheckSudokuSolution import isValid
#
# def main():
#     grid = readSolution()
#
#     if isValid(grid):
#         print("Valid solution")
#     else:
#         print("Invalid solution")
# def readSolution():
#     print("Enter a Sudoku puzzle solution: ")
#     grid =[]
#     for i in range(9):
#         line = input().strip().split()
#         grid.append([eval(x) for x in line])
#     return grid
#
# main()
######################################가장짧은 거리 구하기#################################
# import NearestPoints
# def main():
#     numberpoints = eval(input("Enter the number: "))
#
#     points = []
#     print("Enter",numberpoints,"points",end='')
#     for i in range(numberpoints):
#         point = 2* [0]
#         point[0],point[1] = eval(input("Enter coordinates,separated by comma: "))
#         points.append(point)
#
#     p1,p2 = NearestPoints.nearestPoints(points)
#
#     print("The closest two points are: ",str(points[p1][0]) ,", " ,str(points[p1][1])
#           ," and ",str(points[p2][0]) ,", " ,str(points[p2][1]))
#
# main()

##########################################기본함수############################
# def getMatrix():
#     matrix = []
# 
#     row = eval(input("Enter row :"))
#     col = eval(input("Enter col :"))
#     for i in range(row):
#         matrix.append([])
#         for j in range(col):
#             value = eval(input("Enter value "))
#             matrix[i].append(value)
# 
#     return matrix
# 
# def accumualte(m):  #row모두 더하는 함수
#     total = 0
#     for row in m:
#         total+=sum(row)
# #
# def Sum(m):           #모든 원소값 더하기
#     total = 0
#     for row  in range(len(m)):
#         for col in range(len(m[row])):
#             total += m[row][col]
#     print("Total is ",str(total))
#
# 
# def main():
#     m = getMatrix()
#     print(m)
# 
#     print("Sum of all elements is",accumualte(m))
# main()