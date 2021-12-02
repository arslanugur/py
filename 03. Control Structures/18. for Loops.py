# The for loop is used to iterate over a given sequence, such as lists or strings.
# The code below outputs each item in the list and adds an exclamation mark at the end:
movies = ["Interstellar", "Inception", "Prestige", "Tenet"]
for movie in movies:
    print(movie + " by Nolan!")
# output:
Interstellar by Nolan!
Inception by Nolan!
Prestige by Nolan!
Tenet by Nolan!

# In the code above, the word variable represents the corresponding item of the list in each iteration of the loop.
# During the 1st iteration, word is equal to "hello", and during the 2nd iteration it's equal to "world", and so on.


# Example:
test = [5,3,4,2] 
counter = 0 
max_range = len(test)-1 
while counter <= max_range: 
    test[counter]+= 2 
    counter += 1 
    print(test)
# output:
# [7, 3, 4, 2]
# [7, 5, 4, 2]
# [7, 5, 6, 2]
# [7, 5, 6, 4]

# to create a valid for loop.
letters = ['a', 'b', 'c']
for l in letters:
  print(l)
# output:
# a
# b
# c
  
# Example:
numbers=['20', '22', '26'] 
for n in numbers: 
    print(n) # Output: 20 22 26  
  

# The for loop can be used to iterate over strings.
# For example:   
str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count) # 2

# The code above defines a count variable, iterates over the string and calculates the count of 't' letters in it. 
# During each iteration, the x variable represents the current letter of the string.
# The count variable is incremented each time the letter 't' is found, 
# thus, at the end of the loop it represents the number of 't' letters in the string. 

# Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump to the next iteration.

# for those wondering how For first t, count +=1 So count = 0+1 = 1 For second t, count +=1 So count = 1+1 = 2 So the output is 2

# Example:
list = [2, 3, 4, 5, 6, 7]
for x in list:
    if(x%2==1 and x>4):     # This statement means if the variable x modulus 2 is 1 and variable x is greater than 4 
        print(x)
        break
# output: 5

# Explaination:
# x%2 means that after x is divided by 2 there is a remainder of 1. 
# the "AND" in the if condition means that both parts have to be satisfied, 
# so we can automatically exclude 2, 3, and 4 since they are <= 4 not >4 That leaves 5, 6, and 7 
# Since the for loop works from left to right in the list, let's start with 5 5/2 is 2 remainder 1, 
# so 5%2 =1 and 5>4 so it satisfies the if condition, so the answer is 5! 
# Because of the 'break', even though 7 also fits the if condition, it will not be printed.



# FOR versus WHILE
# Both, for and while loops can be used to execute a block of code for multiple times.
# Loops: The construct can be used to iterate through a list

# It is common to use the for loop when the number of iterations is fixed. 
# For example, iterating over a fixed list of items in a shopping list.

# The while loop is used in cases when the number of iterations is not known and depends on some calculations and conditions in the code block of the loop.
# For example, ending the loop when the user enters a specific input in a calculator program. 

# Both, for and while loops can be used to achieve the same results, 
# however, the for loop has cleaner and shorter syntax, making it a better choice in most cases.

# Example:
words=["Hello","world","spam","eggs"] 
a=0 
b=len(words)-1  # 4 - 1 = 3 
while a<=b: 
    c=words[a] 
    print(c+"!") 
    a=a+1

# Second Way
words = ["hello", "world", "spam", "eggs"]     # 1. words = list with 4 elements
counter = 0                        # 2.
max_index = len(words) - 1         # 3.
while counter <= max_index:     
    word = words[counter]          # 4.     
    print(word + "!")     
    counter = counter + 1          # 5. add 1 to counter, next time through, counter will be item 1 in the list

    
# Third Way
words = ["hello", "world", "spam", "eggs"]

for i in range(0,len(words) ):
    print (words[i] + "!")

# Shorter Way
words = ["hello", "world", "spam", "eggs"]

for i in words:
    print(i + "!")

    
    
# Example:
x=[1,2,3,4,5] 
y=0 
while y<len(x): 
    print(x[y]) 
    y+=1    # 12345


# for loops can be used for lists

# Example: list without for loop
numbrs = [1, 2, 3, 4]
print(num[0])
print(num[1])
print(num[2])
print(num[3])


# Example: list with for loop
numbrs = [1, 2, 3, 4]
for num in numbrs:
    print(num)  # to write some code within the scope of the for loop
                # to throw every element (variable) in the list into "num" and return them in for loop
for a in numbrs:# The for loop returns, as much as the number of elements of the list 
    print('from 1 to 4, written the same thing four times')

    
# Example:
names = ['Joseph', 'George', 'Daniel', 'Charles', 'Victor']

for name in names:
    print(f'My name is {name}')


# Example:
list = [1, 2, 3]
for var in list:
    print(var)


# Example: What if we print a string expression 
name = 'Revolution'# each element is treated as an array element 
for n in name:
    print(n)        # string is printed one under the other


# Example:
tuple = (1, 2, 3, 4, 5)
for t in tuple:
    print(t)

tuple = [(1, 2),(3, 4),(5, 6), (7, 8)] # each list element corresponds to a tuple list 
for t in tuple:
    print(t)

tuple = [(1, 2),(3, 4),(5, 6), (7, 8)] 
for a, b in tuple:
    print(a) # only corresponds to "a" are printed 


# Example: Dictionary List {key : value}
d = {'k1': 1, 'k2': 2, 'k3': 3} 
for item in d:
    print(item) # in this way, only key information comes 

for item in d.items(): # element groups are accessed one by one 
    print(item)

for key, value in d.items():
    print(key)

for key, value in d.items():
    print(key, value)






# Example:
# Manipulating a view 
# I would say that this is useful for the ones having problems with loops.

from string import *

chars = ascii_letters + digits + "_"
pword = (input() or "Simple").replace(" ","")
new = ""

print("[Program started]\n\n")
print("Iterating...\n\n")
print("-->")
while 1:
  
  if new == pword:
    break
  
  else:
    for i in pword:
      for j in chars:
        if i == j:
          new += i
          print(f"-->{new}")
          break
      
        else:
          print(f"[{j}]")
          continue 
    
print(f"\n\nPassword - {new}")
print("\n[Program finished]")


