# Function Examples
# Example: to Display Calendar

# Python has a built-in function, calendar to work with date related tasks. 
# You will learn to display the calendar of a given date in this example. 

# In the program below, we import the calendar module. 
# The built-in function month() inside the module takes in the year and the month and displays the calendar for that month of the year.

# Source Code: Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2014  # year
mm = 11    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
"""
Output
   November 2014
Mo Tu We Th Fr Sa Su
             1  2
3  4  5  6 7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
"""
# You can change the value of variables yy and mm and run it to test this program for other dates.


