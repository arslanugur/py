# String Format
      # https://www.it-swarm-tr.com/tr/python/python-string-formatlamada-s-ve-d-arasindaki-fark-nedir/970513249/

# %d – integer
# %f – float
# %s – string
# %x – hexadecimal
# %o – octal
  
# Examples: Python program to demonstrate the use of formatting using % 
  
# Initialize variable as a string 
variable = '15'
string = "Variable as string = %s" %(variable) 
print(string)                                                       # Variable as string = 15
  
# Printing as raw data  
print("Variable as raw data = %r" %(variable))                      # Variable as raw data = '15'
  
# Convert the variable to integer 
# And perform check other formatting options 
  
variable = int(variable) # Without this the below statement will give error. 
string = "Variable as integer = %d" %(variable) 
print(string)                                                       # Variable as integer = 15
print("Variable as float = %f" %(variable))                         # Variable as float = 15.000000
  
# printing as any string or char after a mark 
# here i use arslan as a string 
print ("Variable as printing with special char = %carslan" %(variable))       # Variable as printing with special char = arslan
  
print("Variable as hexadecimal = %x" %(variable))                   # Variable as hexadecimal = f
print("Variable as octal = %o" %(variable))                         # Variable as octal = 17


