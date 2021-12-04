# Example: which number is bigger from two numbers?
numbera = int(input('number a: '))
numberb = int(input('number b: '))

result = numbera > numberb # it will be true-false - if the value true, the value  olursa a değeri büyük
print(f'number a: {numbera} is bigger than number b: {numberb}: {result}') 



# Example: from the user, calculate the average of two midterms (%60) and one final (%40) grades
midterm1 = float(input('1st midterm: '))  # may input decimal number, thats why using float 
midterm2 = float(input('2nd midterm: '))
final = float(input('final: '))


# Example: if 'average' equals 50 and above (true), it will pass. otherwise fail (false)
average = (((midterm1 + midterm2) / 2) * 0.6) + (final * 0.4)
print(f'Grade Average: {average} and Passing Status: {average>=50} ')
# if blocks could be better for this problem


# Example: to print whether a inputted number is odd or even
number = int(input('number: '))
oddeven = (number % 2 == 0) # modulus equals 0, then even --> by dividing results 0
print(f'situation of the entered number: {oddeven}')



# Example: to print whether a inputted number is positive or negative
number = int(input('number: '))
positive = (number > 0) # if it comes true --> positive, false --> negative
print(f'situation of the entered number: {positive}')


# Example: to request password and mail info, check authenticity
# mail@gmail.com password: mail --> user registry from database
email = 'mail@gmail.com' 
password = 'mail'

enteredMail = input('email: ') # input will be already string, conversion is not necessary
enteredPass = input('password: ')

isMail = email  == enteredMail
# isMail = (email  == enteredMail.lower())         # in case it is written with upper letter wrongly, we use the 'lower' method
# isMail = (email  == enteredMail.lower().strip()) # in case it is written with upper letter wrongly and use unnecessary space wrongly, we use the functions 'lower' and 'strip'
# deletes the spaces we inputted value the begin, the end of 'str' with strip method
isPass = password == enteredPass    # comes true / false to the questions
print(f'email info verification: {isMail} and password verification: {isPass} ')

