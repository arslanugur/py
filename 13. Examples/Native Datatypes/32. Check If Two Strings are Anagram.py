# Native Datatypes Examples
# Example: to Check If Two Strings are Anagram


# Two strings are said to be anagram if we can form one string by arranging the characters of another string. 
# For example, Race and Care. Here, we can form Race by arranging the characters of Care.
# Python program to check if two strings are anagrams using sorted()

str1 = "Race"
str2 = "Care"

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")

# Output: race and care are anagram.

# We first convert the strings to lowercase. It is because Python is case sensitive (i.e. R and r are two different characters in Python).

# Here,
#   lower() - converts the characters into lower case
#   sorted() - sorts both the strings

# If sorted arrays are equal, then the strings are anagram.


