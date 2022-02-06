# Functional Programming Examples:
# Example:
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)

print(len(list(nums)))  # 2

# Explanation:
nums = {1,2,3,4,5,6} # nums is a set --> A set of numbers from 1 to 6
# builds intersection with &: 
nums = {0,1,2,3} & nums # & will only include values that both sets have.
                        # The & is the intersect command that keeps item that is in both set: {0, 1, 2, 3} & {1, 2, 3, 4, 5, 6} = {1, 2, 3} 
# nums = {1, 2, 3}      # The intersection is {1,2,3}
nums = filter(lambda x: x > 1, nums) # filter is used to remove values that are not needed --> Filters out item that is greater than 1.
# list(nums) = [2, 3] 
print(len(list(nums))) # It's asking you to print out the length of nums. = 2


# Example:
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)

print(power(2, 3))      # 8
# commentssss
