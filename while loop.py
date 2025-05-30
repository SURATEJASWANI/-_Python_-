# 1)Display count down timer from 10 to 0 using while loop?

n=10
while n>=0:
    print(n, 'secs')
    n-=1


# 2)Find max digit in number s=2569 using while loop?

n=int(input('Enter number'))
max=0
while n>0:
    dig=n%10
    if max > dig:
        max = dig
    n//=10
print(max)


# 3)simulate a basic login system (max attempts 3)
# Input=['kumar','202','84558906' ]

import random
while True:
    m=''
    res=['kumar','202','84558906' ]
    for x in range (2):
        p=random.choice(res)
        m+=p
    s=input('enter num')
    
    if s==m:
        print('correct')
        break
    else:
        print('wrong')