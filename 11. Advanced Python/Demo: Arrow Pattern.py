def pattern(n):
  for i in range(n*2):
    if i<n:
      print(2*n" "+i*"*")
    elif i>n:
      print(2*n*" "+(n*2-i)*"*")
    else:
      print(3*n*"*")

pattern(5)

"""
          *
          **
          ***
          ****
***************
          ****
          ***
          **
          *
"""


