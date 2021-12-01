# Example: Check driving license situation
# To request a name, age and degree from the user 
# Driving License Conditions: at least 18 age, at least high school

name = input('your name: ')
age = int(input('your age: '))
degree = input('your degree: ')

if (age >= 18) and (degree == 'high school' or degree == 'university'):     # this code value must be true
    print(f'{name}, you can get driving license') # using f string
else:
    print('you cant get driving license')
    

# Example: why cant you get driving license
name = input('your name: ')
age = int(input('your age: '))
degree = input('your degree: ')

if (age >= 18):
    if (degree == 'high school' or degree == 'university'): 
        print(f'{name}, you can get driving license')
    else:
        print('you cant get driving license because of degree')
else:
    print('you cant get driving license because of age')



# Example: print the grade information corresponding to the grade range 
#          according to the average of two exams and one interview
#  0 - 24     --> 0
# 25 - 44     --> 1
# 45 - 54     --> 2
# 55 - 69     --> 3
# 70 - 84     --> 4
# 85 - 100    --> 5
exam1 = float(input('examOne: '))
exam2 = float(input('examTwo: '))
speech = float(input('interviewGrade: '))

average = (exam1 + exam2 + interviewGrade) / 3

if (average >= 0) and (average <= 24):
    print(f'Your average is {average} and your score: 0')
elif (average >= 25) and (average <= 44):
    print(f'Your average is {average} and your score: 1')
elif (average >= 45) and (average <= 54):
    print(f'Your average is {average} and your score: 2')
elif (average >= 55) and (average <= 69):
    print(f'Your average is {average} and your score: 3')
elif (average >= 70) and (average <= 84):
    print(f'Your average is {average} and your score: 4')
elif (average >= 85) and (average <= 100):
    print(f'Your average is {average} and your score: 5')
else:                               # all except the value max. 100 above
    print('you gave a wrong info')  # Range will be maximum 100


    
# Example:
# Calculate the service time of a vehicle whose traffic release time is taken from the user according to the following information
# how many days the vehicle has been in traffic?
# E.g. The difference between 20.11.2010 and the current date should be subtracted as "days" 
# Query by day --> next subject: datetime module shoul be used for this example
#  the first maintenance    -> 1. year
#  the second maintenance   -> 2. year
#  the third maintenance    -> 3. year

# Day-based calculation according to the day, month, year information taken into the duration account
days = int(input('how many days your vehicle in traffic?: '))

if days <= 365:                             # 365 days is accepted as service interval
    print('1st service time')
elif (days > 365) and (days <= 365 *2):     # if it is between one year and two years
    print('2nd service time')
elif (days > 365 * 2) and (days <= 365 *3): # if it is between two years and three years
    print('3rd service time')
else:                                       # the other inputs will be indicated as wrong info except the conditions above
    print('error usage duration in traffic')


# Example: using datetime module
import datetime

date = str(input('which date did your vehicle start being in traffic? (2019/8/9): ')) 
date = date.split('/')              # incoming/inputted date information is separated by slash with the split method 
print(date[0]) # year
print(date[1]) # month
print(date[2]) # day                # why separated? because subtraction will be done

today = datetime.datetime.now()     # to get today's date in today variable 
# print(today)                      # to show today's date
# An object is prepared to subtract
# Prepare a date object named entranceTraffic with datetime module 
entranceTraffic = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
minus = today - entranceTraffic
# print(minus)
# minus yani fark değişkeni içinden days bilgisini alman gerekli
# You need to get 'day information' from minus (subtract variable) 
# print(minus.days)     # 'day information' will be indicated but it is not the goal
days = minus.days       # to get into the 'days' object, so it only takes the day information, not the time or anything. 
#sonrasında koşullu işlemlere geç

if days <= 365:
    print('1st service time')
elif (days > 365) and (days <= 365 *2): 
    print('2nd service time')
elif (days > 365 * 2) and (days <= 365 *3):
    print('3rd service time')
else: 
    print('error usage in traffic')


# Clean Example:
import datetime 

date = str(input('which date did your vehicle start being in traffic? (2019/8/9): ')) 
date = date.split('.')

today = datetime.datetime.now()
entranceTraffic = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
minus = today - entranceTraffic
days= minus.days

if days <= 365:
    print('1st service time')
elif (days > 365) and (days <= 365 *2): 
    print('2nd service time')
elif (days > 365 * 2) and (days <= 365 *3):
    print('3rd service time')
else: 
    print('error usage in traffic')



