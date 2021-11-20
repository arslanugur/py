# The item at a certain index in a list can be reassigned.
# For example:
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums) # [7, 7, 5, 7, 7]

# You can replace the item with an item of a different type.

a = ['x' , 'y']
b = a
b[0] = 'z' 
print(b) # ['z' , 'y'] 
print(a) # ['z' , 'y'] 

# Example:
moviequote = ['Frankly','my','dear','I','don\'t','give','a','hoot'] 
moviequote[7] = 'damn' 
print(moviequote)

# while Example:
nums = [7, 7, 7, 7, 7] 
x = 0 
while x < len(nums): 
    nums[x] = 5 
    x += 1 
    print(nums) 
# for Example:
nums = [7, 7, 7, 7, 7] 
for x in range(len(nums)): 
    nums[x] = 5 
    print(nums)

    
    
# Case1: 
nums = [7, 77, 77] 
nums[2] = 5 
print(nums)       # [7, 77, 5] 
# Case 2: 
nums = [7, 77, 77] 
print(nums[2][1]) # TypeError: 'int' object is not subscriptible
# Case 3: 
nums = [7, 77, "77"] 
print(nums[2][1]) # 7 
# Case 4: 
nums = [7, 77, "77"] 
nums[2][1] = 5 
print(nums)       # TypeError: 'str' object does not support item assignment 
  
        
# Case 1:
a = [1,2,3,4,5] 
a[1:4]= ["a","b","c"] 
print(a)         # [1, 'a' , 'b' , 'c' , 5] 
# Case 2:
a = [1,2,3,4,5] 
reassign = ["a","b","c"] 
a[1:4]= reassign 
print(a)         # [1, 'a' , 'b' , 'c' , 5]

# Example:
nums = [7, 7, 7, 7, 7]
nums[:2] = 1,2,3 
nums[3:5]= 4,5 
print(nums) # 1,2,3,4,5,7

# Example:
nums = [7, 7, 7, 7, 7]
nums[2] = input('Add number')
print(nums)

# Example:
x = [7,7,7,7,7]
x = [5 for i in x]
print(x) # [5,5,5,5,5]

# Example:
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())
items[num]="x" 
print(items)

# Example:
x = 1 
nums = [7, 7, 7, 7, 7] 
for i in nums: 
    a = nums.index(i) 
    nums[a] = a*x+x 
    print(nums)

    
# A simple calculator, using list and if function: 
a=int(input('enter first number: ')) 
b=int(input('enter second number: ')) 
operation= input('enter the operation needed: ')
c=['+', '-','*','/'] 
if operation==c[0]: 
    print('your answer is: ' , a+b) 
if operation==c[1]: 
    print('your answer is: ' , a-b) 
if operation==c[2]: 
    print('your answer is: ' , a*b) 
if operation==c[3]: 
    print('your answer is: ' , a/b)
    
# Example:
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])  # we are assigning nums[1] to nums[3]. That means 2 in the place of 4





    
    
    
    
