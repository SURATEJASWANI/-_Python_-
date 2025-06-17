#<----------------------------------------------------------SLICE METHOD Problems---------------------------------------------------------->

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


# 2. 

v='haadya'
print(v[2:len(v)])   #adya  --> till last(length)
print(v[2:5])        #ady

#(or)--------------------------------------------------------(or)

v='haadya'
for i in range(2,len(v)):
    print(v[i], end='')   #adya
    print(v[i])                # return line by line 
                                        # a
                                        # d
                                        # y
                                        # a
#(or)--------------------------------------------------------(or)

v='haadya'
tm=''
for i in range(2,len(v)):
    tm+=v[i]                    #''+a   a+d     ad+y    ady+a
print(tm)                       #adya
#(or)--------------------------------------------------------(or)

v='haadya'
def fun(v='', start=0, end=len(v), step=1):
    tm=''
    end= end if end<=len(v) else len(v)     # if end value is inputed more, then (error - out of index) will appear, if we inputed more than the length value then the default it will take len()  --> then we should write a condition in ternary operator to take the default value
    for i in range(start, end, step):
        tm+=v[i] 
    return print(tm)
fun('haadya',2,6,1)

j='tejaswani'
fun(j,2,100,1)          # end value =100, so more than len() value, so default len() is taken

x=''
fun(x,6,1)              # as default is defined if no value is passing, still we do not receive error

#<----------------------------------------------------------CONCATENATION Problems---------------------------------------------------------->
    
for i in range(5):
    print('*'*i)

# return -->
# *
# **
# ***
# ****
