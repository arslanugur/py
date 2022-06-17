# 01. Introduction to Sets
def average(array):
    uniq = set(array)
    
    return sum(uniq)/len(uniq)



# 02. Symmetric Difference
#!/usr/bin/env python3

if __name__ == "__main__":
    M = int(input().strip())
    set_m = set(map(int, input().strip().split(' ')))
    
    N = int(input().strip())
    set_n = set(map(int, input().strip().split(' ')))
    
    for el in sorted(set_m ^ set_n):
        print(el)



# 03. Set .add()
#!/usr/bin/env python3

if __name__ == "__main__":
    N = int(input().strip())
    stamps = set()
    
    for _ in range(N):
        stamp = input().strip()
        stamps.add(stamp)
        
    print(len(stamps))



# 04. Set .discard(), .remove() & .pop()
#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split())) 
    num_cmds = int(input())
    
    for _ in range(num_cmds):
        cmd = list(input().strip().split(' '))
        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
    
    print(sum(s))



# 05. Set .union() Operation
#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input().strip())
    english = set(map(int, input().strip().split(' ')))
    m = int(input().strip())
    french = set(map(int, input().strip().split(' ')))
    
    print(len(english.union(french)))



# 06. Set .intersection() Operation
#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input().strip())
    english = set(map(int, input().strip().split(' ')))
    m = int(input().strip())
    french = set(map(int, input().strip().split(' ')))
    
    print(len(english.intersection(french)))



# 07. Set .difference() Operation
#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input().strip())
    english = set(map(int, input().strip().split(' ')))
    m = int(input().strip())
    french = set(map(int, input().strip().split(' ')))
    
    print(len(english.difference(french)))



# 08. Set .symmetric_difference() Operation
#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input().strip())
    english = set(map(int, input().strip().split(' ')))
    m = int(input().strip())
    french = set(map(int, input().strip().split(' ')))
    
    print(len(english.symmetric_difference(french)))



# 09. Set Mutations
#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split())) 
    num_cmds = int(input())
    
    for _i in range(num_cmds):
        cmd = list(input().strip().split(' '))
        if cmd[0] == 'intersection_update':
            get_set = set(map(int, input().split(' ')))
            s &= get_set
        elif cmd[0] == 'update':
            get_set = set(map(int, input().split(' ')))
            s |= get_set
        elif cmd[0] == 'difference_update':
            get_set = set(map(int, input().split(' ')))
            s -= get_set
        elif cmd[0] == 'symmetric_difference_update':
            get_set = set(map(int, input().split(' ')))
            s ^= get_set
    
    print(sum(s))



# 10. The Captain's Room
#!/usr/bin/env python3

if __name__ == "__main__":
    k = int(input().strip())
    numbers = list(map(int, input().strip().split(' ')))
    
    print((sum(set(numbers))*k - sum(numbers))//(k-1))



# 11. Check Subset
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(len((A - B)) == 0)



# 12. Check Strict Superset
if __name__ == "__main__":
    A = set(map(int, input().strip().split(' ')))
    t = int(input().strip())
    superset = True
    
    for _ in range(t):
        subset = set(map(int, input().strip().split(' ')))
        if len(subset - A) != 0 or len(A - subset) == 0:
            superset = False
            break
    
    print(superset)



# 13. No Idea!
#!/usr/bin/env python3

if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))
    
    for el in arr:
        if el in good:
            happiness += 1
        elif el in bad:
            happiness -= 1
    
    print(happiness)


