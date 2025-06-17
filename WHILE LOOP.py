#<----------------------------------------------------------WHILE LOOP Problems---------------------------------------------------------->

# ✅ Basic Level
# 1.Print numbers from 1 to 10 using a while loop.

n=0
while n<=10:
    print(n)
    n+=1

# 2.Print even numbers between 1 and 50 using a while loop.

n=0
while n<=50:
    if n%2==0:
        print('n is even', n)
    n+=1

# 3.Print the multiplication table of a given number (e.g., 5) using a while loop.

n=5
k=1
while k<=10:
    print(n, 'x', k, '=', n*k)
    k+=1

# 4.Calculate the sum of digits of a number using a while loop.
# e.g., 123 → 6


n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("Total sum of digits is:",tot)


# 5.Reverse a number using a while loop.
# e.g., 123 → 321

n=int(input('enter a num'))
reverse=0
while n>0:
    digit=n%10
    n//=10
    reverse=reverse*10+digit
print(reverse)


# ⚙️ Intermediate Level
# 6.Check if a number is a palindrome using a while loop.
# e.g., 121 → Palindrome

n=int(input('enter a num'))
reverse=0
palindrome=n
while n>0:
    digit=n%10
    n//=10
    reverse=reverse*10+digit
print('Reverse number is', reverse)

if reverse==palindrome:
    print('Number is palindrome')
else:
    print('Not a palindrome')


# 7.Print the Fibonacci series up to N terms using a while loop.



# 8.Count the number of digits in a given number using a while loop.

# 9.Keep asking the user for input until they enter "exit".
# Hint: Use while True: and break.

    

# Create a number guessing game using a while loop

# 10.Keep looping until the user guesses the correct number.

#  Provide hints like "Too High" or "Too Low".




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

a,b=0,1
n=0
while n<=5:
    print(a,b)
    a,b=b, a+b
    n+=1
