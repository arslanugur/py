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

# 09. Designer Door Mat

# 10. String Formatting

# 11. Alphabet Rangoli

# 12. Capitalize!

# 13. The Minion Game

# 14. Merge the Tools!
