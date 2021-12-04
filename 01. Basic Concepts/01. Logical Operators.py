# Example:
x = 5
result = 5 < x < 10
print(result) # comes the value 'false' because x = 5, not x > 5

# Example: Second Way with 'and' operator
x = 6
result = x > 5 and x < 10 # with 'and' operator, if both of situation in the condition is true --> true --> boolean algebra
print(result)             # result --> 'true, true' --> shows 'true' 


# Example: Using 'and operator' for string 
lives = 5
keepPlaying = 'e'  # if the user play a game, we need a info inputted info
result = (lives > 0) and (keepPLaying == 'e') 
# if 'lives' is bigger than 0 and if 'keepPlaying' equals with 'e' --> user keep playing
print(result) # comes true


# Example: using 'or'
x = 5
result = (x > 0) and (x % 2 == 0) # if 'x' is bigger than O and the value equals 0 with modulus 2 --> x is even number
print(result)

result = (x > 0) or (x % 2 == 0) # if you are interested in that only one of them is true --> you can use 'or'
print(result)

# true, false -> true
# false, false -> false olur


# Example: using 'not' operator
x = 5
result = not(x > 0) # if x is positive, result will be true
                    # but we will use 'not' in the code, the result will be false
print(result)


# Example: x is an even number between 5 and 10?
x = 6
result = ((x > 5) or (x < 10)) and (x % 2 == 0) # we asked three questions. if the first one will run with and/or operators, the second one will run with and operator
print(result)



