# Advanced Examples
# Example: to Create a Countdown Timer
# Topics: Python while Loop, Python divmod(), Python time Module

# Example: Countdown time in Python
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(5)

#    The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
#    end='\r' overwrites the output for each iteration.
#    The value of time_sec is decremented at the end of each iteration.


