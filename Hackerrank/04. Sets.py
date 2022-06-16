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

# 06. Set .intersection() Operation

# 07. Set .difference() Operation

# 08. Set .symmetric_difference() Operation

# 09. Set Mutations

# 10. The Captain's Room

# 11. Check Subset

# 12. Check Strict Superset

# 13. No Idea!
