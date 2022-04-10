# SECTION 1: Else
The else statement is most commonly used along with the if statement, but it can also follow a for or while loop, which gives it a different meaning.
With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop).

Example:
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")     #

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")
#

The first for loop executes normally, resulting in the printing of "Unbroken 1".
The second loop exits due to a break, which is why it's else statement is not executed.

# b equals 1 IF 2+2 is an EXACT MATCH with 5, ELSE b equals 2 2+2 = 4 ≠ 5 So, 2+2 is NOT an EXACT MATCH with 5, so b equals 2
# if 2 plus 2 equals 5 b is 1 else b is 2
# b equals to 1, the condition is that if 2+2 ""4"" == 5 else 2 we look it than 4 not equals wich 5 then print (else)
# b=1 if 2+2==5 else 2 2+2=4 which is not equal to 5 so we are going for the else part which is 2!



