# Lists are used to store items.
# A list is created using square brackets with commas separating items.
words = ["Hello", "world", "!"]

# In the example above the words list contains three string items.
# A certain item in the list can be accessed by using its index in square brackets.
# For example:
words = ["Hello", "world", "!"]
print(words[0]) # Hello
print(words[1]) # world
print(words[2]) # !

# The first list item's index is 0, rather than 1, as might be expected.

# Example:
words = ["Hello", "world", "!"] 
print(words[-3]) 
print(words[-2]) 
print(words[-1]) 
# output: Hello world !

# Example:
ele1=3          # ELE = Empty List Element
ele2=4
subele1=4
subele2=6
vec=[ele1,ele2,[subele1,subele2]]
print(vec[2][1])  # sublist element = 6 --> The second set of square brackets is referring to the 2nd element in the sublist.



# Example:
counter=0 
list1=["Hello!", "I'am","Happy","to","see","you",["Why","are","you","me?"]] 
while counter <= (len(list1)-2): 
    print(list1[counter]) 
    counter+=1 
    print("."*20) 
    counter=0 
    while counter <= (len(list1)-1): 
        if counter<=2: 
            print(list1[len(list1)-1][counter]) 
        elif counter <=(len(list1)-2): 
            print(list1[counter-1]) 
        else: 
            print(list1[(len(list1)-1)][3]) 
    counter+=1

# Example:
words = ["Hello", "world", "!"]
#the code below joins list
print("".join(words))
#here an assigned list to new variables
x,y,z=words
print(x,y,z)
#printing the items on different lines
print(x)
print(y)
print(z)

# output:
# Helloworld!
# Hello world !
# Hello
# world
# !

# Example:
a = ["you are a hero","Think again"] 
b= int(input("1+1 = ")) 
if b==2: 
  print(a[0]) # 1+1 = you are a hero
else:
  print(a[1]) # 1+1 = think again
  
# Example:
words = ["Hello", "world", "!"] 
x = 0 
while x < 3: 
    print(words[x]) 
    #x = x+1 Or to get them on the same line. 

words = ["Hello", "world", "!"] 
print(words[0],words[1],words[2])




    
# Question Example:
words = [input(), input(), input()] 
print('My Name is: ' + words[0]) 
print('I was born in: ' + words[1]) 
words[1] = 2018 - int(words[1]) 
print('Thus, my current age is: ' + str(words[1])) 
print('I\'m from: ' + words[2]) 


