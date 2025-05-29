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




