# SECTION 1
# Conditional expressions provide the functionality of if statements while using less code. 
# They shouldn't be overused, as they can easily reduce readability, but they are often useful when assigning variables.
# Conditional expressions are also known as applications of the ternary operator.
# Example:
a = 7
b = 1 if a >= 5 else 42
print(b)    # 1

# The ternary operator checks the condition and returns the corresponding value.
# In the example above, as the condition is true, b is assigned 1. If a was less than 5, it would have been assigned 42.
# Another example:
status  = 1
msg = "Logout" if status == 1 else "Login"

print(msg)      # Logout

# The ternary operator is so called because, unlike most operators, it takes three arguments.

# Notice that if and else are not followed by colons here.
# An old trick without if-then-else: 
# For numerical value (especially good for integers), it is equivalent to: b = (a >= 5) * 1 + (a < 5) * 42 or even shorter 
# but less readable, b = (a >= 5) * (- 41) + 42 or b = 1 + (a < 5) * 41

# b = (a >= 5) * 1 + (a < 5) * 42 If a=6 then, b=(1)*1+(0)*42 b=1 If a=4 then, b=(0)*1+(1)*42 b=42 
# Note: a>=5 evaluates to true if a=6 or greater which is then converted to its numeric value 1.
  
# They said, "The ternary operator is so called because, unlike most operators, it takes three arguments." 
# They actually wanted to say, "it takes three operands" and not "arguments"! Keep in mind...!! 
# Functions or Methods takes arguments; whereas, Operators takes Operands, may be unary, binary or ternary.

# Use in real time: Use the ternary operator to simplify your if-else statements that are used to assign values to variables. 
# The ternary operator is commonly used when assigning post data or validating forms. 
# For example if we were programming a comment form 
# and wanted to ensure that the user entered their email address then we could write something like the following. 
# Example: //is email address specified? 
# Notify customer if not $email_address = (empty($_POST['email'])) ? die('Please enter your email address'): $_POST['email'];
      
# this is like in other languages of C-like syntax: condition ? evaluated if true : evaluated if false 
# The inline loop is based on the same principle
# It's SIMILAR, not equal. Here is: (evaluated if true) if (condition) else (evaluated if false)
# Good but I like more C++ method. Same example in C++, Java, C# and C: 
int a = 7, b = (a >= 5)?1:42; //printFunction(b); print 
# Function can be : 
cout<<b; System.out.println(); Console.WriteLine(); printf();




# Example:
a = 7 
b = 1 
if a >= 5 else 42 
print(b) # 1
a = 4 
print(b) # 1

# WHY is the 2nd line of OUTPUT equal to 1 instead of 42? 
# EDIT: got the following answer to my q. 
# because you have to reassign b value once more after reassigning a. 
# b was calculated before and stays the same until you assign something new to it. 
# apply the same ternary operator after reassigning a and before printing b

# Example:
a=7 
b=1 
if a>=5 else 42 
print(b) # 1 
a=4 
b=1 
if a>=5 else 42 
print(b) # 42
# The b variable is unnecessary. Here is a simpler version: a = 7 print(1 if a >= 5 else 42)

# you can also use if else chaining in ternary operators like. a=2 b=3 if a==1 else 4 if a==2 else 5 print(b) # output=4 because a==2
# I will add a bit to make it more clear: a=2 b=3 if a==1 else 4 if a==2 else 5 
# we need to look at it statement by statement 
# so first statement (b=3 if a==1 else 4) 
# because a==1 failed, so b is 4 
# and it literally becomes like this 
# b=4 if a==2 else 5 
# so b remains 4 because a is indeed equals to 2 and quick example here: 
a=5 b=3 if a<4 else 4 if a>6 else 9 if a==6 else 555 if a//2==1 else 999 print(b) # output : 999
  


# Question:
# What is the value of b?
b=1 if 2+2 == 5 else 2      # 2       ---> if 2 plus 2 equals 5 b is 1 else b is 2 
# b equals 1 IF 2+2 is an EXACT MATCH with 5, ELSE b equals 2 
#               2+2 = 4 ≠ 5 So, 2+2 is NOT an EXACT MATCH with 5, so b equals 2

# b equals to 1, the condition is that if 2+2 ""4"" == 5 else 2 we look it than 4 not equals wich 5 then print (else) I hope helpfull
# b = 1 if 2 + 2 == 5 else 2 \/ \/ 4 == 5 \/ False So, b is equal to 2.
# Answer: 2 Explanation: It says that b is 1 if 2+2=5, otherwise it's 2. Since 2+2 isn't 5, b isn't 1, so it has to be 2.



