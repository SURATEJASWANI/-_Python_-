# 1.	Create a dictionary from two lists:
# a.	keys = ['id', 'name', 'age']
# b.	values = [101, 'John', 25]

keys = ['id', 'name', 'age']
values = [101, 'John', 25]
my_dict=dict(zip(keys, values))
print(my_dict)

--or--

keys = ['id', 'name', 'age']
values = [101, 'John', 25]
p={}
for i in range(len(keys)):
    p[keys[i]]=values[i]
print(p)

# Return ==> {'id': 101, 'name': 'John', 'age': 25}

# 2.	Create a dictionary to store student name and age.

v=dict([('tej',23),('vinu',25),('haadya',24)])
print(v)

--or--
v= {'tej':2,'vinu':25,'haadya':24}
print(v)

--or--

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
