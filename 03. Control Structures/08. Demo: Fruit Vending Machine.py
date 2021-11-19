# Problem 
# Imagine a vending machine that sells fruits. Each fruit has its own number, starting from 0. 
# fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"] 

# Task 
# Write a program for the vending machine, which will take n number as input from the customer and return the fruit with that index. 
# If n < 0 or n > 7 (the index of last fruit), the program outputs "Wrong number". 

# Solution 
fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"] 

input = int(input()) 
if input >= 0 and input <= 7: 
  print(fruits[input]) 
else: 
  print("Wrong number")

  
# Second Way:  
fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"] 
num = int(input()) #your code goes here 

if num == 0: 
  print(fruits[0]) 
elif num == 1: 
  print(fruits[1]) 
elif num == 2: 
  print(fruits[2]) 
elif num == 3: 
  print(fruits[3]) 
elif num == 4: 
  print(fruits[4]) 
elif num == 5: 
  print(fruits[5]) 
elif num == 6: 
  print(fruits[6]) 
elif num == 7: 
  print(fruits[7]) 
else: 
  print("Wrong number")

  
  
