# Example: Check whether input is between 0-100 or not
num = float(input('number: '))
result = (num > 0) and (num <= 100)
print(f'number is between zero and hundred?: {result}')

# Example: Check whether input is between 0-100 or not (with the if block)
num = float(input('number: '))
if (num > 0) and (num <= 100):
    print('number is between 0 and 100.')
else:
    print('number is not between 0 and 100.')


# Example: Check whether the number input is positive even or not
num = int(input('number: '))
result = (num > 0) and (num % 2 == 0)
print(f'Number is positive and even number? {result}')

# Example: Check whether the number input is positive even or not (with the if block)
num = int(input('number: '))
if (num > 0):
    if num % 2 == 0:
        print(f'{num} is positive and even number.')
    else:
        print(f'{num} is positive but its odd.')
else:
    print(f'{num} is negative number.')




# Example: Check to Login with Mail and Password Information
mail = 'mail@gmail.com'
password = '1234'

writtenMail = input('mail: ')
writtenPass = input('pass: ')

result = (writtenMail == mail) and (writtenPass == password)
print(f'Entrance is success. {result}')

# Example: with if statement 
mail = 'mail@gmail.com'
password = '1234'

writtenMail = input('mail: ')
writtenPass = input('pass: ')

if writtenMail == mail:
    if writtenPass == password:
        print('Entry is successful.')
    else:
        print('Password is wrong.')
else:
    print('Mail is wrong')




# Example: to compare entered three numbers by size 
firstNo = int(input('1st Number: '))
secondNo = int(input('2nd Number: '))
thirdNo = int(input('3rd Number: '))

result = (firstNo > secondNo) and (firstNo > thirdNo) 
print(f'1st Number is the biggest number. {result}')
result = (secondNo > firstNo) and (secondNo > thirdNo)
print(f'2nd Number is the biggest number. {result}')
result = (thirdNo > firstNo) and (secondNo < thirdNo)
print(f'3rd Number is the biggest number. {result}')

# Example: with if statement 
firstNo = int(input('1st Number: '))
secondNo = int(input('2nd Number: '))
thirdNo = int(input('3rd Number: '))

if (firstNo > secondNo) and (firstNo > thirdNo):
    print(f'{firstNo} is the biggest number.')
elif (secondNo > firstNo) and (secondNo > thirdNo):
    print(f'{secondNo} is the biggest number.')
elif (thirdNo > firstNo) and (secondNo < thirdNo):
    print(f'{thirdNo} is the biggest number.')





# Example: Calculate average of two midterm (60%) and one final (40%) grades from user
visa1 = float(input('visa1: '))
visa2 = float(input('visa2: '))
final = float(input('final: '))

average = ((visa1 + visa2) / 2) * 0.6 + (final * 0.4)
result = (average >= 50) or (final >= 70)
print(f'Öğrenci ortalası {average} ve geçme durumu {result}')

# Example: with if statement
visa1 = float(input('visa1: '))
visa2 = float(input('visa2: '))
final = float(input('final: '))

average = ((visa1 + visa2) / 2) * 0.6 + (final * 0.4)
# First Altern:
if (average >= 50):
    if (final >= 50):
        print(f'Öğrenci ortalası {average} ve geçme durumu başarılı')
    else:
        print(f'Öğrenci ortalası {average} ama final notu <50 başarısız')
else: 
    print(f'Öğrenci ortalası {average} ve geçme durumu ort. yüzünden başarısız')
                # if the average is greater than 50, look at the final grade. 


# Second Altern:
if (average >= 50):     # if the average is greater than 50, successful without looking at the final grade
    print(f'Öğrenci ortalası {average} ve geçme durumu başarılı')
else:
    if (final >= 70):
        print(f'Öğrenci ortalası {average} ama final notu en az 70 olduğundan geçtin')
    else:
        print(f'Öğrenci ortalası {average} ve geçme durumu ort. yüzünden başarısız')



# Example: Body Mass Index Calculation (BMI) by inputting name, weight, height
#    0 - 18.5   -- Thin
# 18.5 - 24.9   -- Normal
# 25.0 - 29.9   -- Fat
# 30.0 - 34.9   -- Obese
# 35.0          -- Morbid Obese

name = input('Name: ')
kg = float(input('Weight: '))
hg = float(input('Length: '))

massindex = (kg) / ((hg**2) / 10000)    # formula

thin = (massindex >= 0) and (massindex <= 18.4)
normal = (massindex >= 18.5) and (massindex <= 24.9)
fat = (massindex >= 25.0) and (massindex <= 29.9)
obese = (massindex >= 30.0) and (massindex <= 34.9)
morbidobese = (massindex >= 35.0)

print(f' {name} weight index: {massindex} and weight assessment is thin {thin}')
print(f' {name} weight index: {massindex} and weight assessment is normal {normal}')
print(f' {name} weight index: {massindex} and weight assessment is fat {fat}')
print(f' {name} weight index: {massindex} and weight assessment is obese {obese}')
print(f' {name} weight index: {massindex} and weight assessment is morbidobese {morbidobese}')



# Example: Body Mass Index Calculation (BMI) with the if statements 
name = input('Name: ')
kg = float(input('Weight: '))
hg = float(input('Length: '))

massindex = (kg) / ((hg**2) / 10000)  # formula

if (massindex >= 0) and (massindex <= 18.4):
    print(f' {name} weight index: {massindex} and weight assessment is thin.')
elif (massindex >= 18.5) and (massindex <= 24.9):
    print(f' {name} weight index: {massindex} and weight assessment is normal.')
elif (massindex >= 25.0) and (massindex <= 29.9):
    print(f' {name} weight index: {massindex} and weight assessment is fat.')
elif (massindex >= 30.0) and (massindex <= 34.9):
    print(f' {name} weight index: {massindex} and weight assessment is obese.')
elif (massindex >= 35.0):
    print(f' {name} weight index: {massindex} and weight assessment is morbid obese.')
else:
    print('Information is Wrong')


