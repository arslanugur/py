# 01. sWAP cASE
def swap_case(s):
    out = ''
    for ind, let in enumerate(s):
        if let.isalpha():
            if let.islower():
                out += s[ind].capitalize()
            else:
                out += s[ind].lower()
        else:
            out += let
    return out



# 02. String Split and Join
def split_and_join(line):
    return "-".join(line.split(" "))



# 03. What's Your Name?
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))



# 04. Mutations
def mutate_string(string, position, character):
    out = list(string)
    out[position] = character
    return "".join(out)



# 05. Find a string
def count_substring(string, sub_string):
    res = 0
    len_sub = len(sub_string)
    
    for i in range(len(string) - len_sub + 1):
        if string[i:i + len_sub] == sub_string:
            res += 1
        i += 1
        
    return res



# 06. String Validators
if __name__ == '__main__':
    s = input()
    
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))



# 07. Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# 08. Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)



# 09. Designer Door Mat
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1, N, 2): 
    print((i*".|.").center(3*N, "-"))
print ("-WELCOME-".center(3*N, "-"))
for i in range(N - 2, -1, -2): 
    print((i*".|.").center(3*N, "-"))



# 10. String Formatting
def print_formatted(number):
    align = len(bin(number)[2:])
    for num in range(1, number + 1):
        n_dec = str(num)
        n_oct = oct(num)[2:]
        n_hex = hex(num)[2:].upper()
        n_bin = bin(num)[2:]
        print(n_dec.rjust(align), n_oct.rjust(align), n_hex.rjust(align), n_bin.rjust(align))




# 11. Alphabet Rangoli
import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    lines = []
    for row in range(size):
        to_print = "-".join(alpha[row:size])
        lines.append(to_print[::-1] + to_print[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))



# 12. Capitalize!

# 13. The Minion Game

# 14. Merge the Tools!
