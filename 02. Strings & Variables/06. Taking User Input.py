# To get input from the user in Python, you can use the intuitively named input function.
# For example, a game can ask for the user's name and age as input and use them in the game. 

# The input function prompts the user for input, and returns what they enter as a string (with the contents automatically escaped). 
x = input()
print(x)

# Always keep in mind that anything return from input() function is STRING 
# so if you know that you are asking for number and need to treat the input as integer or float, 
# just parse, convert the type in programming, function as follows: 
integer_input = int(input()) 
float_input=float(input())

# Example: to take user input, assign it to a variable, and output it:
text = input()
print(text)

# INPUT
  # The input statement needs to be followed by parentheses.
  # You can provide a string to input() between the parentheses, producing a prompt message.
  # Example
name = input("Enter your name: ")
print("Hello, " + name)   



# Even if the user enters a number as input, it is processed as a string.
name = (input("Enter your name: ")) 
print("I'm " +name+"! ") 
age = int(input("what's your age? ")) 
print("I'm " + int(age) + " years old ")

# The prompt message helps to clarify what input the program is asking for.


# Example:
# Write a program to take two integers as input and output their sum.
# Sample Input: 2, 8
# Sample Output: 10

num1 = int(input())
num2 = int(input())

print(num1 + num2)



