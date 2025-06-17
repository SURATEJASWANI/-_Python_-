#<----------------------------------------------------------SLICE Problems---------------------------------------------------------->

# 1. print input using slice and also input reverse

s='teja'                                                #1 s="teja"
def slice(s, start=0, end=len(s)-1, step=1):            #2 slice(s, start, end, step)  ----> "teja",0,8,1
    for i in range (start, end+1, step):                #5   ---> i=   0     1     2     3      (+1 step)
        print(s[i], end ='')                            #6   ---> s[1]=t     e     j     a
    print()                                             #7   --->      t     e     j     a     -----> returns ==> none & prints ==> teja

def slicerev(s, start=len(s)-1, end=0, step=-1):        #3 slicerev(s, start, end, step)  ---->  "teja",8,0,-1
    for i in range (start, end-1, step):                #9    ---> i=   3     2     1    0      (-1 step)
        print(s[i], end ='')                            #10   ---> s[1]=a     j     a    t
    print()                                             #11   --->      a     j     a    t     -----> returns ==> none & prints ==> ajet

slice(s, 0, len(s)-1, 1)                                #4
slicerev(s, len(s)-1,0,-1)                              #8
