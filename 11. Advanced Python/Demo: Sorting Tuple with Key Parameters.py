# Sorting Tuple with Key Parameters

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)   # Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

