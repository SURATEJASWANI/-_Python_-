# 1.	Create a dictionary from two lists:
# a.	keys = ['id', 'name', 'age']
# b.	values = [101, 'John', 25]

keys = ['id', 'name', 'age']
values = [101, 'John', 25]
my_dict=dict(zip(keys, values))
print(my_dict)

--------------------or--------------------

keys = ['id', 'name', 'age']
values = [101, 'John', 25]
p={}
for i in range(len(keys)):
    p[keys[i]]=values[i]
print(p)

# Return ==> {'id': 101, 'name': 'John', 'age': 25}

--------------------or--------------------

k=['a','b','c']
v=[1, 2, 3]
res={k[x]:v[x] for x in range(len(k))}
print(res)

# Return ==> {'a': 1, 'b': 2, 'c': 3}

# 2.	Create a dictionary to store student name and age.

v=dict([('tej',23),('vinu',25),('haadya',24)])
print(v)

--------------------or--------------------
v= {'tej':2,'vinu':25,'haadya':24}
print(v)

--------------------or--------------------

res={}
res['Name']='tej'
res['age']=21
res['pin']=101
print(res)

# Return ==> {'Name':'tej','age':21,'pin':101}

# 3.	Create an empty dictionary and add key-value pairs one by one.

my_dict=[]
for x in range(3):
  store={}
  store['name']=input('Enter Name:')
  store['age']=input('Enter Age:')
  my_dict.append(store)
print(my_dict)

# Return ==> [{'name': 'tej', 'age': '2'}, {'name': 'vinu', 'age': '3'}, {'name': 'haadya', 'age': '4'}]

# 4.	Get the value of key "salary" from this dictionary:
#                     EX: employee = {'name': 'John', 'age': 30, 'salary': 50000}

employee = {'name': 'John', 'age': 30, 'salary': 50000}
print(employee['salary'])
print(employee.get('salary'))

# Return ==> 50000

# 5.	 Remove the last inserted key-value pair from the dictionary using an appropriate method

employee = {'name': 'John', 'age': 30, 'salary': 50000}
employee.popitem()
print(employee)

# Return ==>{'name': 'John', 'age': 30}

# 6.	Define packing and unpacking in Python. Also, provide one example for both packing and unpacking.

-------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Delete a list of keys from a dictionary
# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# # Keys to remove
# keys = ["name", "salary"]

sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}  #for loop with del
key_delete=["name", "salary"]

for key in key_delete:
    if key in sample_dict:  
        del sample_dict[key]
print(sample_dict)                  

#=> Returns: {'age': 25, 'city': 'New york'}

--------------------or--------------------

sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}  #for loop with pop
key_delete=["name", "salary"]

for key in key_delete:
    sample_dict.pop(key)
print(sample_dict)            

#=> Returns: {'age': 25, 'city': 'New york'}

# 2. Count the frequency of each character in a given string using a dictionary.

var='python dictionary'
temp={}

for x in var:
    temp[x]=1
else:
    temp[x]+=1
print(temp)              

#=> Returns: {'p': 1, 'y': 2, 't': 1, 'h': 1, 'o': 1, 'n': 1, ' ': 1, 'd': 1, 'i': 1, 'c': 1, 'a': 1, 'r': 1}

# 3. Swap keys and values in a dictionary.

org_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
new_dict={value:key for key, value in org_dict.items()}
print(new_dict)                                                                

#=> Returns: {'Kelly': 'name', 25: 'age', 8000: 'salary', 'New york': 'city'}

# 4. Write a program to sum all the values in a dictionary.

input={'a':11,'b':25,'c':34,'d':45}
sum=0
for value in input:
    sum+=input[value]
print(sum)                              

#=> Returns: 115

# 5. Create a nested dictionary for student details (name, roll, marks).

student_details = {
                    "abc": {"roll": 101, "marks": 85},
                    "xyz": {"roll": 102,"marks": 92},
                    "AxByCz": {"roll": 103,"marks": 78},
                    "A1B2": {"roll": 104,"marks": 68} 
                }
print(student_details)

#=> Returns: {'abc': {'roll': 101, 'marks': 85}, 'xyz': {'roll': 102, 'marks': 92}, 'AxByCz': {'roll': 103, 'marks': 78}, 'A1B2': {'roll': 104, 'marks': 68}}

# 6. Convert a dictionary to a list of tuples.

h={'a':1,'b':2,'c':3,'d':5,'e':6}
for i in h.items():
    print(i, end=' ')      
    
# => Returns: ('a', 1) ('b', 2) ('c', 3) ('d', 5) ('e', 6) 

# 7. Write a program to store names as keys and their lengths as values.

list=['python', 'developer', 'Java', 'CSS', 'JS']
dict={x: len(x) for x in list}
print(dict)                                           

# => Returns: {'python': 6, 'developer': 9, 'Java': 4, 'CSS': 3, 'JS': 2}

--------------------or--------------------

list=['python', 'developer', 'Java', 'CSS', 'JS']
dict={}

for x in list:
    dict[x]=len(x)
print(dict)                                            

# => Returns: {'python': 6, 'developer': 9, 'Java': 4, 'CSS': 3, 'JS': 2}

# 8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and
# "odd" if the number is odd
# Expected Output:
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

num=int(input("enter num?"))
data={}
for x in range(1,num+1):
    if x%2==0:
        data[x]='even'
    else:
        data[x]='odd'
print(data)                         

# => Returns:  {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd'}               

# 9. Create Reverse Word Dictionary
# Given list of words:
# words = ["cat", "dog", "bat"]
# Create a dictionary with words as keys and their reversed strings as values
# Expected Output:
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

words = ["cat", "dog", "bat"]
reverse={}

for i in words:
    reverse[i]=i[ : :-1]
print(reverse)                      

#=> Returns: {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

--------------------or--------------------

words = ["cat", "dog", "bat"]
d={}
for i in words:
    res=""
    for j in i:
        res=j+res
    d[i]=res
print(d)

#=> Returns: {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

#--------------------------------------------------------------------------------------------------------------------------------------------

1. Invert a dictionary with list values (group keys by their values)
Input:
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
Output:
{1: ['a', 'c'], 2: ['b'], 3: ['d']}
(Hint: Use setdefault method)
2. Find Max and Min Value in Dictionary
Input:
d = {'a': 10, 'b': 5, 'c': 15}
Output:
Max Value → 15
Min Value → 5
3. Create a dictionary using dictionary comprehension for the given list of numbers,
where:
• Each number is a key.
•
The value is "prime" if the number is prime.
•
The value is "notprime" if the number is not prime.
 Output: {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}
4. Create a dictionary from a list of words, keys as words, values as word lengths, but
only for words longer than 3 characters
 List: ["hi", "hello", "world", "is", "great"]
5. Create a dictionary with uppercase letters as keys and their ASCII values as values use
dict comprehension .
Input: letters = ['a', 'b', 'c']
Expected Output:
{'A': 65, 'B': 66, 'C': 67}
6. Explain about setdefault function in dictionary data type ?
7. Difference between d[key] and d.get(key)?
8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with
examples.
