# 1.	Write a Python program that takes an amount n = 5200 and breaks it down into the minimum number of currency notes available in                         denominations of 500, 200, 100, 50, 20, 10, and 1 rupees.
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


