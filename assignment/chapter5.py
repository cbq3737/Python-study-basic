##############################13번########################################
Line =10
count =0
for i in range(100,201):
    if i% 5 ==0 and i % 6==0:
        print(end='')
    elif i % 5==0 or i % 6 ==0 :
        print(i, end = ' ')
        count += 1
        if count % 10 ==0:
            print()

#############################20번#####################################
a
count = 0
for i in range(1,7):
    count+=1
    for j in range(1,count+1):
        print(j,end=' ')
    print()

b
count =9
for i in range(1,7):
    count-=1
    for j in range(1,count-1):
        print(j,end=' ')
    print()

c
count=7
for i in range(1,7):
    count-=1
    for j in range(1,count):
        print(" ",end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

# ################20번################
count = 0
i = 1
sum =0
while count<100000:
    sum += 4*((-1)**(i+1)/(2*i-1))
    i+= 1
    count+=1
    if (i-1) % 10000 == 0:
        print("i가", i-1, "일때 i의 파이 근삿치값은: ", sum)
