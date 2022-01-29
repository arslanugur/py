'''This is an example of what a decorator may be useful for.
In this code a decorator function (elapsed_time) was used to calculate the time elapsed while executing the primary function (big_sum).
The primary function itself calculates the sum of the integer numbers from 0 to 99999 (incl.). It takes some time for the function to return the result, since the numbers range is quite big.
The decorator function acts as a wrapper:
    - it records the system time before the primary function is called (t1)
    - then it calls the primary function f()
    - then it records the system time right after the primary function execution is finished (t2)
    - it calculates the difference between t1 and t2 and prints it
Thus, shoud you ever need to calculate the time of your function execution, you may simply grab the 'elapsed_time' function from the code below, add it to your code, and then decorate the function the execution time of which you'd like to calculate with @elapsed_time. Please remember to import the 'time' module, since this decorator uses it.
Thus, decorators increase the code reusability.
'''

import time

def elapsed_time(f):
    def wrapper(*n):
# *n for any arguments in the primary function
        t1 = time.time()
        f(*n)
# *n for any arguments in the primary function
        t2 = time.time()
        el_time = (t2 - t1) * 1000
        print('Elapsed time: {}  ms'.format(el_time))
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 1000000)):
        num_list.append(num)
    print('Big sum: {}'.format(sum(num_list)))

def main():
    big_sum()

if __name__ == '__main__': main()

  
