# Native Datatypes Examples
# Example: to Convert String to Datetime

# Example 1: Using datetime module
from datetime import datetime

my_date_string = "Mar 11 2011 11:31AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)

# Output:
# <class 'datetime.datetime'>
# 2011-03-11 11:31:00

# Using strptime(), date and time in string format can be converted to datetime type. 
# The first parameter is the string and the second is the date time format specifier.

# One advantage of converting to date format is one can select the month or date or time individually.

# If you want to learn more about the directives and strptime(), please go to Python strptime() - string to datetime object.
# Example 2: Using dateutil module
from dateutil import parser

date_time = parser.parse("Mar 11 2011 11:31AM")

print(date_time)
print(type(date_time))

# Output:
# 2011-03-11 11:31:00
# <class 'datetime.datetime'>

# Using dateutil module, parse() can be used to convert a string into date time format. The only parameter used is the string.



