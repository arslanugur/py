# A while loop is used to repeat a block of code multiple times.
# For example, we need to process multiple user inputs, so that each time the user inputs something, the same block of code needs to execute.

# Below is a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates. 
i = 1           # the starting value is 1 --> the starting value is less than the last value
while i <=5:
    print(i)
    i = i + 1   # i (1) equals i + 1, or 1 + 1 since i is one. Then the command restarts at while, with i as 2.

print("Finished!")
# 1 2 3 4 5 Finished!

# During each loop iteration, the i variable will get incremented by one, until it reaches 5.
# So, the loop will execute the print statement 5 times.

# The code in the body of a while loop is executed repeatedly. This is called iteration.

# Loop 1: Replacing i with a number: while i <=5: while 2 <=5: print(i) print(2) i = i + 1 i = 2 + 1 
# Because i is now 2, the system continues to loop because 2 is still less than 5. 
# When it loops again, will become 3, since 2 (i) + 1 is 3. The system loops until i becomes 5. 
# The system stops after i is 5 because any number higher than 5 will not be true in <=5. 
# For example: if i was 6, the command would have no output, since 6 is higher than 5. 
     
# Example:
i = 3
while i>=0:
   print(i)     # output: 3 2 1 0
   i = i - 1    # print(i) comes AFTER i = i - 1

# Explain 
# i = 3 
# while 
# i >= 0 ------------------------------ i = i - 1 --------> means i = 2 
# i >= 0 is True, thus repeat execution i = i - 1 --------> means i = 1 
# i >= 0 is True, thus repeat execution i = i - 1 --------> means i = 0 
# i >= 0 is True, thus repeat execution i = i - 1 --------> means i = -1
# i >= 0 is False, thus loop ends here 
              
 
# Example:
a = 8
while a >= 0:
    print(a) 
    a = a - 2   # output: 8 6 4 2 0

# Example to Edit:
i = 4 
while i <=5: 
    print(i) 
    i = i - 1 
    # print("Finished!") 


# You can use multiple statements in the while loop.
# For example, you can use an if statement to make decisions. 
# This can be useful, if you are making a game and need to loop through a number of player actions and add or remove points of the player.
# The code below uses an if/else statement inside a while loop to separate the even and odd numbers in the range of 1 to 10: 
# Example:
x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1 
# output:
# 1 is odd
# 2 is even
# ...
# 9 is odd
    
# str(x) is used to convert the number x to a string, so that it can be used for concatenation.
# In console, you can stop the program's execution by using the Ctrl-C shortcut or by closing the program.

# Example:
# Example: prints the even values.
x = 0
while x <=20:
    print(x)
    x += 2
    # output: 0 .. 20

    
# BREAK STATEMENT
  # To end a while loop prematurely, the break statement can be used.
  # For example, we can break an infinite loop if some condition is met:
i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")
# output:
# 0
# 1
# 2
# 3
# 4
# Breaking
# Finished


#1 i = 0.it prints out the i (0) adds 1 to i (0 + 1) i now equals 1 Loop 
#2 i = 1 it prints out the i (1) adds 1 to i (1 + 1) i now equals 2 Loop 
#3 i = 2.it prints out the i (2) adds 1 to i (2 + 1) i now equals 3 Loop 
#4 i = 3 it prints out the i (3) adds 1 to i (3 + 1) i now equals 4 Loop 
#5 i = 4 it prints out the i (4) adds 1 to i (4 + 1) i now equals 5 Since i = 5, 
# the if statement starts (if i >= 5:). It then immediately breaks. 
# Output: 0 1 2 3 4 Now the reason why 0 gets displayed 
# and 5 doesn't is because of this: 
#Loop 
#1 "it prints out the i (0) and this: Loop #5 "it prints out the i (4) adds 1 to i (4 + 1) i now equals 5 
# Since i = 5, the if statement starts (if i >= 5:). It then immediately breaks." 
# if you want the 1 and 5 to be displayed, swap print(i) i = i + 1 to get: i = i + 1 print(i) 


# Explain:
# while True is a short and easy way to make an infinite loop.

# An example use case of break:
# An infinite while loop can be used to continuously take user input. 
# For example, you are making a calculator and need to take numbers from the user to add and stop, when the user enters "stop".
# In this case, the break statement can be used to end the infinite loop when the user input equals "stop". 

# Using the break statement outside of a loop causes an error.

# Example: Password Log
p="Python" 
i=1 
while i<=3: 
    t=input("Enter your password:\n") 
    if p==t: 
        print("Access Granted") 
        break 
    else: 
        print("Access Denied, try again") 
        i+=1 


# Example:
i=1
while 1==1:
    print("*"*i)
    i=i+1
    if i>=4:
        break
i=i-1
while 1==1:
    i=i-1
    print("*"*i)
    if i==0:
        break
# output:
*
**
***
**
*


# Example:
i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break
# output: 5 4 3    
# first 5 is printed. then it is decreased to 4. as it is not satisfying i<=2,it moves on. then 4 is printed. 
# then it is decreased to 3. as it is not satisfying i<=2,it moves on. then 3 is printed . then it is decreased to 2. 
# as now i<=2 has completely satisfied....the loop breaks.

# Second Way 
i=5
count=0;
while True:
 print(i)
 count=count+1;
 i=i-1
 if i<=2:
  break 
print('Printing the number '+str(count)+' times.');


# CONTINUE STATEMENT
# Another statement that can be used within loops is continue.
# Unlike break, continue jumps back to the top of the loop, rather than stopping it. 
# Basically, the continue statement stops the current iteration and continues with the next iteration.

# For example:
i = 1
while i<=5:
  print(i)
  i += 1
  if i==3:
    print("Skipping 3")
    continue
# output:
# 1
# 2
# Skipping 
# 3
# 4
# 5    
    
# An example use case of continue:
# An airline ticketing system needs to calculate the total cost for all tickets purchased. 
# The tickets for children under the age of 1 are free. 
# We can use a while loop to iterate through the list of passengers 
# and calculate the total cost of their tickets. 
# Here, the continue statement can be used to skip the children. 

# Using the continue statement outside of a loop causes an error.

# Continue = skip
# Break = stop    
    
# Example:

# Example: Monster vs Hero
monster = 30 
steel_axe = 1 
fighting = True 
while fighting: 
  monster = monster - 1 
  print("You attacked the monster! HP left:") 
  print(monster) 
  if monster == 15: 
    print("He's halfway dead!") 
    continue 
  elif monster == 10: 
    print("Take him down!") 
    continue 
  elif monster == 5: 
    print("Now's your chance") 
    continue 
  if monster <= 0: 
    print ("Dead!") 
    break
    print("Congrats!")


# Example:
i = 300 
while 1==1 and i>=235: 
    print(str(i) + " rich guy") 
    i -= 5 
    while i<235: 
        print(str(i) + " running out, slow down") 
        i -= 10 
        if i<=0: 
            print("bankrupt") 
            break 
            print("Told you")



# Fibonacci Example:  
n = 0 
i = 1 
print(i) 
while i <50: 
  y = n+i 
  print(y) 
  n = i 
  i = y 
  print("Fibonacci!")

  
# Example:
age = 1 
while True: 
    age = age +1 
    if age == 16: 
        print("you cant date yet") 
        continue 
        if age == 18: 
            print("Breaking") 
            break 
            print(age) 
            print("alright, date whom ever you want")

            
# Example:
items = [23, 555, 666, 123, 128, 4242, 990] 
sum = 0 
n = 0 
while n < len(items): 
  num = items[n] 
  n += 1 
  if num % 2 != 0: 
    continue 
    sum += num 
    print(sum)  # no output


# Example to edit:
i = 0
while i <= 5:
    i += 1
    if i == 2:
        # пропускаем индекс цикла 2
        # и продолжаем с 3
        continue
    if i == 3:
        print("line", i, "next")
    if i == 5:
        print("stop while")
        #  прерываем цикл
        break
    # цикл не прерываем, потому что i 
    # не равно 5 - печатаем i
    print(i)

print("Finished")
# output:
# 1
# line 3 next
# 3
# 4
# stop while
# Finished


# Example to edit: Street Fighter  
player = int(input()) 
health = 100 
enemy = 100-player

while True: 
  if enemy >= 1 and enemy <= 99: 
    print("there is an enemy!\n!stay alert!") 
    break 
  if enemy <= 0: 
    print("Nice Shot") 
    break


# Example to edit:
i = 0 
while True: 
    i = i +1 
    if i == 2: 
        print(("Skipping ")+str(i)) 
        continue 
    if i == 5: 
        print(("Breaking at ")+str(i)) 
        break 
        print(i) 
        print("Finished")
      
# Example to edit
i = int(input("how much money do you have?: ")) 
while i >= 5: 
    print("youarerich") 
    i -= 1 
    print("but now you have") 
    print(i) 
else: 
        print("now you are poor !!") 
        print("i hve taken all your money, goodbye")     


      
# Example to edit
n=0 
i=2 
x=int(input("input a number: ")) 
while i<=x: 
    if (x%i == 0): 
        n+=1 
        i+=1 
        if n==1: 
            print("It is a prime number.") 
        else: 
            print("It is not a prime number.")
            
            
    
# Example: Fibo Short nested version. 
i = 1 
p = 1 
while i <=5: 
  print(i) 
  i = i + 1 
  while p <=5: 
    print(p) 
    p = p + 1 
    print("Finished!") 

  
  
# Multiplication Example:
x=int(input('write the number and a multiplication table: ')) 
print('\n') 
print('multiplication table '+'of '+str(x)) 
print('\n') 
y=x 
while y<=x*10: 
    print(y) # 5 10 15 ...
    y=y+x

# Multiplication Example:
a=int(input('which number table do you want: '))
i=1 
while i<=10: 
    print(int(a),'x',int(i),'=',int(a*i)) 
    i=int(i+1) 
    # input: let a is assigned 5 (ie a=5)
    # output: 5 x 1 = 5 ...


# Example to edit:
i = 1 j = 1 k = 1 while k <=10: print(i) print (j) i = i + j j = i + j k = k + 2 
print("Fibonacci!") 
#loop 1 #print("i") == 1 #print("j") == 1 #i = i + j: i = 1 + 1 => i == 2 #j = i + j: j = 2 + 1 => j == 3 #k = k + 2: k = 1 + 2 => k == 3 <= 10 
#loop 2 #print("i") == 2 #print("j") == 3 #i = i + j: i = 2 + 3 => i == 5 #j = i + j: j = 5 + 3 => j == 8 #k = k + 2: k = 3 + 2 => K == 5 <= 10 
#loop 3 #print("i") == 5 #print("j") == 8 #i = i + j: i = 5 + 8 => i == 13 #j = i + j: j = 13 + 8 => j == 21 #k = k + 2: k = 5 + 2 => k == 7 <= 10 
#loop 4 #print("i") == 13 #print("j") == 21 #i = i + j: i = 13 + 21 => i == 34 #j = i + j: j = 34 + 21 => j == 55 #k = k + 2: k = 7 + 2 => k == 9 <= 10

# Example to edit
n = int(input()) 
sum=0 
while n > 0: 
  x=n % 10 
  sum += x 
  n=n //10 
  print(sum)        
        
        
        instant death - ani ölüm
        korku aklı öldürür
        
