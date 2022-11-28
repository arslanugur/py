# 01. itertools.product()
#!/usr/bin/env python3

from itertools import product

if __name__ == "__main__":
    arr1 = list(map(int, input().strip().split(' ')))
    arr2 = list(map(int, input().strip().split(' ')))
    
    for el in product(arr1, arr2):
        print("{} ".format(el), end='')



# 02. itertools.permutations()
#!/usr/bin/env python3

from itertools import permutations

if __name__ == "__main__":
    in_data = list(input().strip().split(' '))
    
    for el in permutations(sorted(in_data[0]), int(in_data[1])):
        print("".join(el))
        
        
# 03. itertools.combinations()
#!/usr/bin/env python3

from itertools import combinations

if __name__ == "__main__":
    in_data = list(input().strip().split(' '))
    
    for lng in range(1, int(in_data[1])+1):
        for el in combinations(sorted(in_data[0]), lng):
            print("".join(el))
            
            
            
# 04. itertools.combinations_with_replacement()
#!/usr/bin/env python3

from itertools import combinations_with_replacement

if __name__ == "__main__":
    in_data = list(input().strip().split(' '))
    
    for el in combinations_with_replacement(sorted(in_data[0]), int(in_data[1])):
        print("".join(el))
        
        
# 05. Compress the String!
#!/usr/bin/env python3

from itertools import groupby

if __name__ == "__main__":
    #in_data = input().strip().split(' ')
    
    for el, el_list in groupby(input()):
        print((len(list(el_list)), int(el)), end=' ')
        
        
# 06. Iterables and Iterators
#!/usr/bin/env python3

import string
symbols = string.ascii_lowercase

from itertools import combinations

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(str, input().strip().split(' ')))
    times = int(input().strip())
    cmbts = list(combinations(sorted(arr), times))
    
    print("{:.4f}".format(len(list(filter(lambda a: a[0] == 'a', cmbts)))/(len(cmbts))))
    
    
# 07. Maximize It!
#!/usr/bin/env python3

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))


