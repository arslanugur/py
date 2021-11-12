# IN-PLACE OPERATORS
  # In-place operators allow you to write code like 'x = x + 3' more concisely, as 'x += 3'.
  # The same thing is possible with other operators such as -, *, / and % as well. 
x = 2
print(x)  # 2

x += 3    # to add 8 to the current value of x
print(x)  # 5
          # x += 3 or x = 3 + x actually means, (new value of x) = 3 + (old value of x)

  # I have x = 1 And i want x += 2 
  # So first of all, what does (x +=2) mean? 
  # (x += 2) is the same as (x = 2 + x) 
  # This means that the final answer for x that we want it from the sequence x += 2 will be x=2+1 
  # It's just like a normal math problem, you take the x value which is 1 and put it in this equation x=2+x 
  # It will be x = 2+1 Then you just add them together and get x=3 
  # It could also be solved like this: x=5 x+=9 x=9+5 x=14

  # Saying x = x + 2 looks like a mistake, because logically, if x = x + 2, then 2 = x - x, i.e. 2 = 0, which is impossible. 
  # The answer is that in Python, "=" is an assignment operator. 
  # x = 5 should be thought of as "x is set at the value 5", rather than "x equals 5", 
  # so it's quite ok to say: x = 5 
  # x is set at 5 x = 6 
  # x is set at 6 (and is no longer 5) so "x += 2" means (the new value of x) is set at (the current value of x) + 2" 
  # so x = 3 x += 5 print(x) prints 8 
  # because x = 3 + 5 = 8 To say "x equals 3" we use "x == 3", which comes later under Boolean operators. 

  # Examples:
x = 4
x *= 3
print(x) # 12

x = 22 
x //= 7 
print(x) # 3

  # x += y --> x = x + y 
  # x -= y --> x = x - y 
  # x *= y --> x = x * y 
  # x /= y --> x = x / y 

  # These operators can be used on types other than numbers, as well, such as strings
x = "bugs"
print(x)    # bugs

x += "bunny"
print(x)    # bugsbunny

  # In-place operators can be used for any numerical operation (+, -, *, /, %, **, //).
    
  # if x is "bugs" and y is "bunny", 
  # the strings are "added" (concatenated) together, giving bugsbunny, but the other operators don't work. 
  # If x is a string and y is a number, only *= works. 
  # E.g. if x is "bugs" and y is 2, the string is repeated 2 times, giving bugsbugs, but the other operators don't work.

x = "a"
x *= 3
print(x)      # aaa



# WALRUS OPERATOR
  # Walrus operator := allows you to assign values to variables within an expression, including variables that do not exist yet.
  # (Walrus operator ":=" is used to assign bool or values)
  # Let's suppose we want to take an integer from the user, assign it to a variable num and output it:
num = int(input())
print(num)

  # The walrus operator accomplishes these operations at once: 
print(num:=int(input())) 
  
  # The walrus operator makes code more readable and can be useful in many situations.
  
  # Walrus offers a way to accomplish two tasks at once,
  # assigning a value to a variable, and returning that value,
  # which can sometimes offer a way to write shorter, more readable code, that may even be more computationally efficient.
  
  # to use walrus operator twice
print( (num1:=int(input())) + (num2:=int(input())) )

  # Example
(num:= float(input ())) 
y = num+10.5 
print(y)
  # Input:  2.5
  # Output: 13.0  
  
  # to produce code which takes text as input, assigns it to the name variable, and outputs it.
print(name:= input())
  
  
  # Examples:
  #  Without Walrus operator 
num = int(input()) 
print(num*3) 
  # Input: 5 
  # Output: 15 
  
  # With Walrus Operator 
print(num:= int(input())*3)
  # Input: 10
  # Output: 30
  

  
