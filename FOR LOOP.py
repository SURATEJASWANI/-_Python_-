#<----------------------------------------------------------FOR LOOP Problems---------------------------------------------------------->

#1. Print Multiplication Tables from 1 to 10
#Write a program using nested loops to print multiplication tables from 1 to 10.

for i in range(1,11):
    for j in range(1,11):
        print(i, '*', j, '=', i*j)
    print()
    

#2. Count Prime Numbers Between 1 and 100
#Use nested loops to count how many prime numbers exist between 1 and 100.

for i in range(1,101):
    if i==1 and i==i:
print(i)


# 3. Print All Pairs (i, j) from 1 to n Where the Sum is Even
#Take input n, and print all pairs (i, j) such that i + j is even.


#4. Count Total Number of Factors from 1 to n
#Take input n, and count the total number of factors (divisors) for all numbers from 1 to n.


#5. Find All Pythagorean Triplets ≤ n
#Take input n, and print all combinations (a, b, c) such that a² + b² = c² and all values are ≤ n.


i=9
 match i%2:
    case 0:
        print("x")
    case 1:
        print("y")
    case 2:
        print("xy")
    case _:
        print("exit")


for i in range(1,11):
    print(i*i)

# Print all numbers from 1 to 10 using a for loop.

for i in range(11):
    print(i)


# Print all even numbers between 1 and 20 using a for loop.

for i in range(2,21,2):
    print(i)

# or

for i in range(1,21):
    if i%2==0:
        print(i)

# or

for i in range(1,21):
    rem=i%2
    if rem==0:
        print("even", i)
    else:
        print("odd", i)


# Print the square of numbers from 1 to 5.

for i in range(1,6):
    print(i*i)

# Calculate and print the sum of numbers from 1 to 10.

sum = 0
for i in range(1,11):
    sum += i
    print(sum)

# Print the multiplication table of 5 (from 5×1 to 5×10).

mult=5
for i in range(1,11):
    print(mult, 'x', i , '=' , mult * i)


# Print all odd numbers between 1 and 15.

for i in range(1,16):
    if i%2!=0:
        print(i)


# Print the cubes of numbers from 1 to 7.

for i in range(1,8):
    print(i*i*i)

for i in range(1,8):
    print(i**3)

# Print numbers from 10 to 1 in reverse order.

for i in range(10,0,-1):
    print(i)

# 1.Count how many numbers between 1 and 50 are divisible by 7.

count=0
for i in range(1,51):
    if i%7==0:
        count+=1
        print(i)
print('Number of 7 divisible count =', count)

# 2.Print the factorial of a number (e.g., 5!) using a for loop

number = int(input("enter number"))
factorial = 1

for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")

# 3.print all numbers b/w 1 to 40 which are divisible by both 5 and 7

count=0
count2=0
for i in range(1,41):
    if i%7==0 or i%5==0:
        count+=1
        print(i)
