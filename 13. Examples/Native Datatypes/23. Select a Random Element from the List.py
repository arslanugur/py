# Native Datatypes Examples
# Example: to Randomly Select an Element From the List

# Example 1: Using random module
import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))         # Output: 31

# Using random module, we can generate a random element from a list. 
# As shown in the example above, the list my_list is passed as a parameter to choice() method of random module.

# Note: The output may vary.
  
  
# Example 2: Using secrets module
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))        # Output: c

# Using choice() method of secrets module, you can select a random element from the list.
# It is cryptographically safer than the random module.


