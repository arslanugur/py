# Example:
try:
  print(1)
  print(20 / 0)
  print(2)              # The number is not printedby this code
except ZeroDivisionError:
  print(3)              #
finally:
  print(4)              #
#
# 2 is not printed because the code skipped that line 
# when the ZeroDivisionError caused it to call on the exception line where the program started again with 3 and finished finally with 4


# Example: Open the file in binary write mode
open("test.txt", "wb")
# "w"   for writing and creating file 
# "w+"  for writing,reading and creating f 
# "wb"  for writing in binary and creating b file 
# "wb+" for reading, writing in binary and creating b file


# Example: to try to open and read from a file. Print an error message in case of an exception.
try:
 with open("test.txt") as f:
    print(f.read())
except:
  print("Error")
#
# "with" is used because one wants to make sure the test.txt is closed after being used. 
# f is needed because it's already used in the line below f.read(). -- 'f' is a temporary variable
# I suspect that one can use whichever letter as long as it's used in the following line as well. 
# e.g. One can use with open as k if it is followed by k.read() In order to print an exception "except" has to be used and always ":" needs to be used in the end.


# Example: What is the highest number that would be printed by this code?
try:
  print(1)              #
  assert 2 + 2 == 5
except AssertionError:
  print(3)              # 
except:
  print(4)
#
# num 1 is ready to launch, compiler checks your assertion
# your assertion is false, there's no exception on num 3, num 4 is disappeared



