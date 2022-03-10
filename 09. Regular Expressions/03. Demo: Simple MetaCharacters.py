import re

pattern = r"gr.y"               # Only one character at position 2 (01.3)
pattern2= r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1, starts with gr, any charatcter and then y")

if re.match(pattern2, "grey"):
    print("Match 1 (patern2), starts with gr, any charatcter and then y")
    
if re.match(pattern, "gray"):
    print("Match 2, starts with gr, any charatcter and then y")

if re.match(pattern, "blue"):   # Doesn't start with gr.....
    print("Match 3")

if re.match(pattern, "grayblue"):
    print("Match 4, starts with gr, any charatcter and then y and more")

if re.match(pattern2, "grayblue"):
    print("Match 4, starts with gr, any charatcter and then y and more")
else:
    print("No match patern2 - doesn't ends with 'y'")

if re.match(pattern, "igrayblue"): # Doesn't start with gr.....
    print("Match 5")

print("\nNow, reviewing a list with gr.y")    
searched = ["a", "e", "i", "o", "u", "ai", "bc", 'b', '.']  

for l in searched:            # Reviewing with the list 'searched'
    strin = "gr"+l+"y"          
    value = re.match(pattern, strin)
    if value:
        print(l, value.group())
    else:
        print(l, 'No match')
print("\nNow, increasing the number of letters in the dot place")

for j in range(1, 3):
    for l in searched:
        strin = "gr"+l*j+'y'   # Increasing the number letters to search
        if(re.match(pattern, strin)):
            print('Match   ',l*j , '\t', strin)
        else:
            print('No match',l*j , '\t', strin)
print('Still only one char in position 2 is valid\n\nNow increasing the number of dots')

for k in range(1, 3):
    pattern = r"gr"+'.'*k+'y'   # Increasing the number of "dots" in pattern
    print("\n", pattern)
    for j in range (1, 4):
       for l in searched:
           strin = 'gr'+l*j+'y'
           if(re.match(pattern, strin)):
              print('Match   ', strin)
           else:
              print('No match', strin)
print("Still, only one char per dot in the pattern, but there have to be one")
print("\nNow other way of increase the dot number, creating a range of options (ie: 1-3)")
pattern = r"gr.{1,3}y"  # Another way to increase the number of "dots"
print(pattern)          # This way allows to include a 'range' of 'dots'
for k in range(1, 3):

    for j in range (1, 5):
       for l in searched:
           strin = 'gr'+l*j+'y'
           if(re.match(pattern, strin)):
              print('Match   ', l*j, "\t", strin)
           else:
              print('No match', l*j, "\t", strin)
print()


