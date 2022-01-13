# List Slices Generator - Demo
import random as rnd
import re

# Get slice position order
def get_slice_position(slice_index, slices): 
    if (slice_index == slices[0]):
        return("|1")
    elif (slice_index == slices[1]):
        return("|2")
    else:
        return "-"

# Generate the list
ls = []
while len(ls) < 8:
    n = rnd.randint(0, 7)
    if (not (n in ls)):
        ls.append(n)

# Generate the slice indexes and step
first_slice_index = rnd.randint(0, 7)
second_slice_index = rnd.randint(0, 7)
slice_step = rnd.randint(1, 2)

if (first_slice_index > second_slice_index):
    slice_step *= -1

# Output: Print the list to slice
print("# List to slice", end='\n')
print("ls =", ls)
print("print(ls[%d:%d:%d])" % (first_slice_index, second_slice_index, slice_step))

# Output: Format the solution
space = "   " if (slice_step < 0) else ""
indexes = [i for i in range(8)]
slices = list(map(lambda index: get_slice_position(index, [first_slice_index, second_slice_index]), indexes))
slices = re.sub("[\[\]'' ']", "", str(slices)).replace(",", "  ").replace("-", " ")

print("\n# Solution")
print("# list  ", ls)
print("# index ", re.sub("\D", " ", str(indexes)))
print("# slice %s%s\n" % (space, slices))
print("# Result %s" % ls[first_slice_index:second_slice_index:slice_step])


