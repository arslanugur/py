# Advanced Examples
# Example: to Measure the Elapsed Time in Python
# Topics: Python time Module

# Example 1: Using time module
import time

start = time.time()

print(23*2.3)

end = time.time()
print(end - start)

"""
Output:
52.9
3.600120544433594e-05
"""

# In order to calculate the time elapsed in executing a code, the time module can be used.
#     Save the timestamp at the beginning of the code start using time().
#     Save the timestamp at the end of the code end.
#     Find the difference between the end and start, which gives the execution time.

# The execution time depends on the system.
# Example 2: Using timeit module
from timeit import default_timer as timer

start = timer()

print(23*2.3)

end = timer()
print(end - start)

"""
Output:
52.9
6.355400000000039e-05
"""

# Similar to Example 1, we use timer() method from timeit module.

# timeit provides the most accurate results.


