# Native Datatypes Examples
# Example: to Count the Number of Occurrence of a Character in String


# Example 1: Using a for loop
count = 0

my_string = "Programming"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)    # 2

# In the above example, we have found the count of 'r' in 'Programming'. 
# The for-loop loops over each character of my_string and the if condition checks if each character of my_string is 'r'. 
# The value of count increases if there is a match.
# Example 2: Using method count()
my_string = "Programming"
my_char = "r"

print(my_string.count(my_char))   # 2

# count() counts the frequency of the character passed as parameter.



