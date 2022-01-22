# Longest Word

# Given a text as input, find and output the longest word.

# Sample Input                      # Sample Output
# this is an awesome text             awesome

# Recall the split(' ') method, which returns a list of words of the string.

# Code:
txt = input()

y = txt.split()
a = len(y)

def char(text):
	count=0
	for c in text:
		count+=1
	return count
	
num=[char(y[i]) for i in range(a)]
x = num.index(max(num))
print(y[x])


