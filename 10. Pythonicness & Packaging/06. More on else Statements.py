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


https://www.sololearn.com/learning/1073/2500/5195/2  comments
