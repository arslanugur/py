# Getting in Shape
# Reading files

# Explanation:
# Tom has done pull ups every day and recorded his results. 
# He recorded each day's results in a new line, so that each line represents each day he has done pull ups.
# Create a program that takes n number as input and outputs the n-th days result (starting from 0).

# Sample Input:  4                        # Input:  1                     # Input:  5
# Sample Output: Day 4, 9 pull ups        # Output: Day 1, 8 pull ups     # Output: Day 5, 10 pull ups




# Note: Recall the readlines() function that returns a list containing each line in the file as a list item.


# Code:
file = open("/usercode/files/pull_ups.txt")
n = int(input())

list=file.readlines()
print(list[n])

file.close()



# Code:
file = open("/usercode/files/pull_ups.txt","r")

n = int(input())
for i in file:
    
    b = file.readlines()
    print(b[n-1])

file.close()


