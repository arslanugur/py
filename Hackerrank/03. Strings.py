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

# 05. Find a string

# 06. String Validators

# 07. Text Alignment

# 08. Text Wrap

# 09. Designer Door Mat

# 10. String Formatting

# 11. Alphabet Rangoli

# 12. Capitalize!

# 13. The Minion Game

# 14. Merge the Tools!
