# 01. itertools.product()
#!/usr/bin/env python3

from itertools import product

if __name__ == "__main__":
    arr1 = list(map(int, input().strip().split(' ')))
    arr2 = list(map(int, input().strip().split(' ')))
    
    for el in product(arr1, arr2):
        print("{} ".format(el), end='')



# 02. itertools.permutations()

# 03. itertools.combinations()

# 04. itertools.combinations_with_replacement()

# 05. Compress the String!

# 06. Iterables and Iterators

# 07. Maximize It!
