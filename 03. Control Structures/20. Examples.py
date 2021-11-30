# Example:
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])  # 8
# So, first we have to solve the [list[4] part.
# that's 5. Then the result is (list[5]) and that's 8.


# Example:
for i in range(10):   # for i in range of 0 and 9
  if not i % 2 == 0:  # modulus is remainder after division
    print(i+1)        # print i and plus 1 to i
# Print all the even numbers between 2 and 10
# if i modulus 2 is not equal to 0, if the remainder of i divided 2 isn't 0
# print(i + 1) #  Answer: 1 + 1 = 2 
         # remainder is 1 3 + 1 = 4
         # remainder is 3 5 + 1 = 6 
         # remainder is 5 7 + 1 = 8
         # remainder is 7 9 + 1 = 10 
  
# Example:
while False:
  print("Looping...")
# While statement works by checking if the condition is true. 
# While (condition) == True: 
# While (condition): those two lines operate the exact same way. 
# So this question says: 
# While False == True: 
# False never equals True, so the loop will never run. zero line


# Example: to print the first element of the list, if it contains even number of elements.
list = [1, 2, 3, 4]
if len(list) % 2 == 0:  # print first element if length of list is even. 
  print(list[0])
# output: 1


# Example:
letters = ['x', 'y', 'z']
letters.insert(1, 'w')  # we insert letter 'w' on element 1. The W was placed between x and y 
print(letters[2]) # y


# Example: to iterate over the list using a for loop and print its values.
list = [1, 2, 3]
for var in list:  # The usage of var in this cases behaves a bit like iterator in C++
  print(var)



