nums=[]                   # create an empty list
print('Begin of Program')
i=0                       # the starting value
while i<=10:              # while the starting value goes until 10
    nums=nums+[i]         # the values assign to the empty list called 'nums'
    print(nums)
    i=i+1                 # to increase one by one
i=i-1                     # the values decrease one by one
while i>0:                # while the ending value goes until 0
    del(nums[i])          # to delete one by one
    print(nums)
    i=i-1                 # the values decrease one by one
print("End of Program")

# output:
Begin of Program
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4]
[0, 1, 2, 3]
[0, 1, 2]
[0, 1]
[0]
End of Program


