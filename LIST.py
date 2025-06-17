#<----------------------------------------------------------LIST problems---------------------------------------------------------->

# 1. Sum of Elements:
# Write a program to calculate the sum of all numbers in a list.

x=[3, 10, 15, 20, 90]
num=sum(x)
print(num)


# 2. Find Maximum Element:
# Write a program to find the largest element in a list.

x=[234, 333, 7899, 11111]
c=max(x)
print(c)

# 3. Remove Duplicates:
# Write a program to remove duplicate values from a list while maintaining the order.

x=[2, 67, 45, 33, 2, 56, 67, 3, 33]
num=[]                                
for i in x:
    if i not in num:
        num.append(i)
print(num)

# 4. Reverse a List:
# Write a program to reverse a list without using built-in methods.

x=['efef', 979, 3689, 'euiefi']
rev=[]
for i in range(len(x)-1,-1,-1):
    rev.append(x[i])
print(rev)

# 5. Count Element Frequency:
# Write a program to count how many times each element appears in a list.

x=[3, 10, 15, 20, 90, 33, 47]
for i in x:
    count=x.count(i)
    print(i, '==>', count,'times')

# 6. Filter Even Numbers:
# Write a program to extract all even numbers from a list.

x=[3, 10, 156, 20, 90, 33, 47]
for i in x:
    if i%2==0:
        print(i)


# 7. Merge Two Lists:
# Write a program to merge two lists into one without using the + operator or extend().

x=[1,2,3,4,5]
y=[6,7,8,9,10]
merge=x+y
print(merge)
