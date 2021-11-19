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

  
  
