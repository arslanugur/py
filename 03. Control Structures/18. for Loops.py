# The for loop is used to iterate over a given sequence, such as lists or strings.
# The code below outputs each item in the list and adds an exclamation mark at the end:
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")
# output:
hello!
world!
spam!
eggs!

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
    if(x%2==1 and x>4):
        print(x)
        break
# output: 5


