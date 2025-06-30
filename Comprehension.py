#LIST--------------------------------------------------------------------------------------------------------------------------------------------LIST

# 1.	Write a Python program that takes an amount n = 5200 and breaks it down into the minimum number of currency notes available in                         
#denominations of 500, 200, 100, 50, 20, 10, and 1 rupees.
#Output: 10 500rupees notes and 1 200rupees notes

m=5200
if m>0:                        #true
  digit=m//500                 #5200//500===> 10
  print(f'{digit} {500} rupees note')
  m%=500
if m>0:
  digit1=m//200
  print(f'{digit1} {200} rupees note')
  m%200
if m>0:
  digit2=m//100
  print(f'{digit2} {100} rupees note')
  m%100
if m>0:
  digit3=m//50
  print(f'{digit3} {50} rupees note')
  m%50

#==> outcome ['10 500 rupees note']
#['1 200 rupees note']

# 2.	Write a Python program to keep asking the user to enter a password until they enter the correct

while True:
  m=input('enter password:')
  if m=='xyz@1234'
  


# 3.	 Convert a 2D list into a flat 1D list using list comprehension.

# 4.	Given a string, use list comprehension to create a list of all characters, excluding vowels.

# 5.	From a given list of words, extract only those that start with a vowel (a, e, i, o, u).
#Example:
#words = ["functions", "loops", "oops", "exception", "as"]

m=["functions", "loops", "oops", "exception", "as"]
res=[x for x in m if x[0] in 'aeiouAEIOU']
print(res)

#6. checking and counting down the amount

n= 5400
f=[500,200,100,50,20,10]
res=[]
for x in f:                              #500              #400
  digit=n//x                             # 5400//500==> 10 # 400//200
  if digit>0:                             # true           # true
    res.append(f'{digit} {x} rupees note') #10             #2
    n%=x                                  #5400%=500==>  400 #400%=200 ==> 0        (reminder)
print(res)

#==> outcome ['10 500 rupees note' , '2 200 rupees note']

#7. string --> int

k='123'
h='012345'
result=0

for x in k:
  for y in range(len(h)):
    if x==h[y]:
      result=result*10+y
print(result)
print(type(result))

#==>123
#  <class 'int'>

#8. [[1,2],[3,4],[5,6]]

res=[[x,x+1] for x in range(1,6,2)]
print(res)                              #==> [[1,2],[3,4],[5,6]]

res=[[x,x+1,x+2] for x in range(1,8,3)]
2	print(res)                            #==>[[1,2,3],[4,5,6],[7,8,9]]

#9. Write a program where we can find the input no. of days into years, months, days

j=395
if j>0:
  data=j//365
  if data>0:              # skips if the value is 0 (zero)
    print(data,'years')
    j%=365
if j>0:
  data1=j//30
    if data1>0:
    print(data1,'months')
    j%=30
if j>0:
  data2=j//7
  if data2>0:
    print(data2, 'week')
    j%=7
if j>0:
  print(j,'days')

#==> 1 years
#    1 months
#    1 days


#--------------------------------------------------------------------------------------------------------------------------------------------
# 1.	Flatten the nested list [[1, 2], [3, 4], [5, 6]] into a single list.
# 2.	From a nested list [[2, 5], [7, 9], [12, 15]], extract all even numbers.
# 3.	Create a list of squares for numbers from 1 to 20.
# 4.	Print prime numbers between 10 to 20 using list comprehension?
# 5.	Convert a=10 int data type to 10 string data type  with out using str()?
# 6.	Write a Python program to swap the case of each character in a given string without using the built-in swapcase() method.
# 7.	Write a list comprehension to print only the word 'python' from the list.
#                      S=[ ‘python’ ,’java’ , ‘c++’ , ‘developer’ ]

#TUPLE--------------------------------------------------------------------------------------------------------------------------------------------TUPLE
# 1.	Access the value 200 from this nested tuple?
#                       t = (10, 20, (30, 40, (100, 200)), 50)
# 2.	Access the value 70 from the nested structure?
#                    data = (10, (20, 30, (40, 50, (60, 70))), 80)
# 3.	Convert   j=(10,20,30,40,50)  tuple data type to list data type?
# 4.	Find Common Elements Between Two Tuples
#          t1 = (1, 2, 3, 4)
#          t2 = (3, 4, 5, 6)
#--------------------------------------------------------------------------------------------------------------------------------------------
# 1.	nums = [5, 12, 17, 24, 35, 40, 55]
#               Create a tuple containing only numbers that are divisible by 5 using comprehension.

# 2.	Given a string: "HelloWorld" Create a tuple of all uppercase letters present in the string using comprehension.?
# 3.	marks = [55, 72, 48, 90, 67]
#             Create a tuple where each element is "Pass" if marks are >= 50 else "Fail" using comprehension.?

# 4.	Given a sentence: "Python is powerful and easy to learn"
#             Create a tuple of words that have more than 4 characters using comprehension.

# 5.	students = [("Alice", 85), ("Bob", 45), ("Charlie", 60), ("David", 30)]
#                Create a tuple containing names of students who scored 50 or more using comprehension


#--------------------------------------------------------------------------------------------------------------------------------------------


1.	What is List Comprehension? Give an Example.?
2.	What are  *args   and **kwargs  give an example? 
3.	What is break and continue and pass in python , give an example?
4.	Difference between list and tuple in python? 
5.	Combine two lists index-wise:
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
Output: [1, 'a', 2, 'b', 3, 'c']
6.	Find all pairs in a list whose sum is equal to a given number target = 10:
lst = [2, 4, 6, 3, 5, 7, 8]
7.	What is the difference between shallow copy and deep copy give an example? 
8.	Create a list of tuples (number, square) for numbers from 1 to 5 using list comprehension in python?
9.	Replace negative numbers with 0 using list comprehension:
EX: nums = [-2, 3, -5, 6]
10.	Print the Primary Diagonal Elements of a list?
Lis= [
    	[1, 2, 3],
    	[4, 5, 6],
    	[7, 8, 9]
    ]
   Expected output: [1, 5, 9]

11.	Write a Python program to find the character that appears the most number of times in a given string.
    N=fullstack developer
