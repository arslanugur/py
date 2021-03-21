# a = min([sum([11, 22]), max(abs(-30), 2)])

a = min(
    [
        sum([11, 22]),  #33
        max(
            abs(-30),   #absolute value of -30 is 30
            2      #between 30 and 2, 30 is bigger max = 30
            )
    ]   #a = min([33, 30])
    )   #a = 30

print(a)

#####

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print('All larger than five')

if any([i % 2 == 0 for i in nums]):
    print('At least one is even')

for v in enumerate(nums):
    print(v)


#######

nums = [-1, 2, -3, 4, -5]
if all ([abs(i) < 3 for i in nums]):
    print(1)
else:
    print(2)
    