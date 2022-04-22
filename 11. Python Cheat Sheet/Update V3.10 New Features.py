# Explanation: https://docs.python.org/3.10/whatsnew/3.10.html

# BETTER ERROR MESSAGES
x = 30
if x = 6:
  
# old version output: SyntaxError: invalid syntax
# new Version output: SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?


# MATCH CASE (like Switch Case in Java)
  #we do not say if equals equals anymore
x = input("")
y = int(input(""))
match x:
  case "hi":
    print("1")
  """
  case "hi" | "bye":   #or operator
    print("1")
    
  case "hi" if y < 10: #with variable y
    print("1")
  case "hi":
    print("Other 1")  
  """  
  
  case "hello":
    print("2")
    
  case _:            #Default case in Java: output for anything to write except hi or hello
    print("Something else") 
    
# Union Operator 
from typing import Union

def myFunc(x: Union[int, float]): -> Union[int, float]:   
    #we dont need to use def myFunc(x: int | float) -> int | float:
      return x ** 2

print(myFunc(10))  #output: 100



