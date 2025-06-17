# Question (1).	 Reverse a given string.(with index and with out index)
    
#---> with index

h='Haadya'
resverse=''
for x in h:
    resverse=x+resverse
print(resverse)

#---> without index

h='Haadya'
resverse=''.join(reversed(h))
print(resverse)   


# Question (2).	 Check whether a string is palindrome or not. (with reversing and with out reversing )

#--> reversing

palindrome='rotator'
reverse=''
for x in palindrome:
    reverse=x+reverse
result='palindrome' if reverse==palindrome else 'not palindrome'
print(result)

#--> with out reversing

palindrome='Haadya'
reverse=''.join(reversed(palindrome))
result='palindrome' if reverse==palindrome else 'not palindrome'
print(result,'==>', {reverse})

# Question (3).	 Count total number of vowels in a string.

x='characters'
vowels_count=0
for i in x:
    if i in 'AEIOUaeiou':
        print(i)
        vowels_count+=1
print(vowels_count)

# Question (4).	Convert all letters of a string to upper case.

x='upper case letters'
result=x.upper()
print(result)

# Question (5).	 Remove all spaces from a string.

x='space removal'
rem=x.replace(' ','')
print(rem)

# Question (6).	Check whether a string contains only alphabets.

alphanum='1965 DwfG VklQA'
b=alphanum.isalpha()
print(b)

# Question (7).	Count the number of words in a sentence.

num='abcdefgh ijklmnop'
num1=num.split()
print(len(num))         #gives the indexing length of each letter  - 17 including space
print(len(num1))        #gives the indexing of word  -- 2

# Question (8).	Find the  non-repeating character in a string.

x='non-repeating character'
for i in x:
    if x.count(i)==1:
        print(i)

# Question (9).	Write all the Python string methods and for each method Mention its main feature or functionality Form a sentence using that method to demonstrate its use.

# Question (10).	Write a Python script to separate upper case letters and lower case letters from a given string. Also form a sentence to explain what your code does.

x='PythOn sCriPt to sepAratE uPpEr cAse letTerS aNd lOweR cAse leTteRs'
upper_case=''
lower_case=''
for char in x:
    if char.isupper():
        upper_case+=char
    else:
        lower_case+=char
print(upper_case)
print(lower_case)

# Question (11).	Swap the case of all letters in a string.

x='PythOn sCriPt to sWap uPpEr cAse letTerS aNd lOweR cAse leTteRs'
swap=x.swapcase()
print(swap)

# or

upper_case=''
lower_case=''
for char in x:
    if char.isupper():
        upper_case+=char
    else:
        lower_case+=char
print(upper_case)
print(lower_case)

# Question (12).	Write a Python code to add an underscore ‘@’before each capital letter in a given string

x='Python code to add an underscore'
y='Python code to add an underscore'.split()
new='_'.join(x)
new1='@'.join(y)
print(new)                                      # return == P_y_t_h_o_n_ _c_o_d_e_ _t_o_ _a_d_d_ _a_n_ _u_n_d_e_r_s_c_o_r_e
print(new1)                                     # return == Python@code@to@add@an@underscore

x='Python code to add an underscore'
new='_'.join(x).split()
print(new)                                   # return == ['P@y@t@h@o@n@', '@c@o@d@e@', '@t@o@', '@a@d@d@', '@a@n@', '@u@n@d@e@r@s@c@o@r@e']

# Question (13). write a program to get the repeated character in a string.

v='haadya'
once=set()                      # {h +a +d +y}
repeat=set()                    # {a}
for chr in v:                   # h     a       a       d       y       a
    if chr in once:             # ❌    ❌     ✔       ❌      ❌      ✔
        repeat.add(chr)         # ❌    ❌      a       ❌      ❌      ✔
    else :
        once.add(chr)           # h     a               d       y
print(repeat,'==&&==', once)    # return --> {'a'} ==&&== {'h', 'd', 'a', 'y'}
