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


# Example:
countries =[Germany, Russia, England] 
print(countries) 
    # The result will be Germany Russia England but if you specify it like 
# print(countries[0]) The result will be Germany

# Example:
nums = [5, 4, 3, 2, 1]
print(nums[1])  # 4
# 5=[0] 4=[1] 3=[2] 2=[3] 1=[4]

# Example:
j=[1,2,3] 
i=["1","2","3"] 
print(j[1]) 
print(i[1])


# EMPTY LIST
# Sometimes you need to create an empty list and populate it later during the program. 
# For example, if you are creating a queue management program, 
# the queue is going to be empty in the beginning and get populated with people data later.

# An empty list is created with an empty pair of square brackets. 
empty_list = []     
print(empty_list)   # []
    # Function returned square bracket because the list has been treated as string. When you have: x=["a"] print(x[0]) will return a print(x) will return ['a']

# Explanation:    
    # it is still a list
print(type(empty_list)) # <class 'list'> 

empty_list = "[]" 
print(empty_list) # [] 
    # now it is a string
print(type(empty_list)) # <class 'str'> 
    # so here empty list is working as a variable.    
    
    
# In some code samples you might see a comma after the last item in the list. It's not mandatory, but perfectly valid.



# Typically, a list will contain items of a single item type, but it is also possible to include several different types.
# Lists can also be nested within other lists. 
number = 3
things = ["string", 0, [1, 2, number], 4.56]    # nested list
print(things[1])     # 0
print(things[2])     # [1, 2, 3]
print(things[2][2])  # 3

# Nested lists can be used to represent 2D grids, such as matrices.
# For example:
m = [
    [1,2,3],
    [4,5,6]
    ]
    
print(m[1][2]) # 6

# A matrix-like structure can be used in cases where you need to store data in row-column format. 
# For example, when creating a ticketing program, the seat numbers can be stored in a matrix, with their corresponding rows and numbers.
# The code above outputs the 3rd item of the 2nd row.

# Example:
things[2] = [1,2,3] 
things[2][0] # 1 
things[2][1] # 2 
things[2][2] # 3 

# Example:
things=["string",0,[1,2,3],4.56] 
things[0]   # string 
things[1]   # 0 
things[2]   # [1,2,3] -->  things[2] = [1,2,3] 
things[3]   # 4.56 
 
# Example:
number = 3 
things = ["string", 0, [1, 2, number], 4.56] 
print(things[0][0]) # s
print(things[0][1]) # t
print(things[0][2]) # r
print(things[0][3]) # i
print(things[0][4]) # n
print(things[0][5]) # g --> things[0] refers to ["string"]

# Example: to create a list and print its 3rd element.
list = [42, 55, 67]
print(list[2])

# Some types, such as strings, can be indexed like lists.
# Indexing strings behaves as though you are indexing a list containing each character in the string.
# For example:
str = "Hello world!"
print(str[6])   # w
# Space (" ") is also a symbol and has an index.

# Trying to access a non-existing index will produce an error.
# Example:
num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
print(num[5])   # Error

# strings, can be indexed 
# int = 654 print(int[0]) --> integers cant! 
# float = 6.04554 print(float[2]) --> float will not be indexed too! 
int = 654
print(str(int)[0])   # 6 
float = 0.12345 
print(str(float)[1]) # .
print(str(float)[2]) # 1

# Example:
str = "Hello world!" 
i = 0 
while i<len(str): 
    print(str[i])   # print(str[5]*i,str[i])
    i = i+1 
    # Output: H e l l o w o r l d !

# 1. Strings are Lists (of characters) and can be nested inside lists just like other lists. 
# 2. You can use "in" operator both for Lists and Strings. 
# 3. You can use adding and multiplication for both Lists and Strings.
# 4. Strings are unchangable meaning that you cannot replace a character with other characters in a list. 
# Eg:
# Str='Hi'
# Str[0]='P' Error 
# 5. Lists are changable and you can replace the members easily. 
# Eg: 
# List=[1,'hi',[2,3,['bye']]]
# List [2][2][0]='hi'
# print(List) [1,'hi',[2,3,['hi']]]

# Example:
str = "she believed" 
print(str[1] + str[2] + " " + str[6] + str[7] + str[8] + str[11]) # he lied
    
# Example:
x = 'python'
y = x[::-1] 
print(y) # nohtyp

# Example:
int = 1234567 
x = str(int)
print(x[4]) # 5


# Example:
num=[5,4,3,[10,9,8,7],1]
print(num[0]) #output: 5 
print(num[1])
print(num[2])
print(num[3]) #output: [10,9,8,7]
print(num[4])
print(num[3][2]) #output: 8 
# prints the 3rd item in the nested list.
# the [3] points to the nested list and the [2] points to the 3rd item in the list which is 8.



# Q Example:
my_list = [0, 1, 2, 3, 4] 
i = 0 
while i<5: 
    print (my_list[i]) 
    i += 1 


# Question Example:
words = [input(), input(), input()] 
print('My Name is: ' + words[0]) 
print('I was born in: ' + words[1]) 
words[1] = 2018 - int(words[1]) 
print('Thus, my current age is: ' + str(words[1])) 
print('I\'m from: ' + words[2]) 



