#<----------------------------------------------------------NESTED LOOP problems---------------------------------------------------------->

#1. print sets whose sum is 5

for i in range(6):      #0              #1
    for j in range(6):  #0,1,2,3,4,5     0,1,2,3,4,5
        if (i+j)==5:    #0+5=True        1+4
            print(i,j)  #0 5             1 4            2 3    3 2    4 1    5 0

#2. print sets which are diviible by both 3 & 5

for i in range(6):
    for j in range(6):
        if (i%3==0) and (j%3==0):
            print(i,j)
        elif (i%5==0) and (j%5==0):
            print(i,j)

#(or)-------------------------------(or)

for i in range(6):
    for j in range(6):
        if (i%3==0) and (j%3==0):
            print(i,j)

#3. print sets of range from 5-5 inner & outer loops

for i in range(6):         #0                         1                       2                       3                       4......5......
     for j in range(6):    #0,1 0,2 0,3 0,4 0,5       1,0 1,2 1,3 1,4 1,5     2,0 2,2 2,3 2,4 2,5     3,0 3,2 3,3 3,4 3,5
          print(i,j)       #

#4. print when the sum is odd

for i in range(1,11):
        for j in range(1,11):
                x=i+j
                if x%2!=0:
                        print(i,j)

#5. print when the sum is even

for i in range(1,11):
        for j in range(1,11):
                x=i+j
                if x%2==0:
                        print(i,j)
