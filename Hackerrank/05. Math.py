# 01. Polar Coordinates
#!/usr/bin/env python3

import cmath

if __name__ == "__main__":
    cnum = complex(input().strip())
    
    print(abs(cnum))
    print(cmath.phase(cnum))



# 02. Mod Divmod
output = divmod(int(input().strip()), int(input().strip()))
print(output[0])
print(output[1])
print(output)



# 03. Power - Mod Power
#!/usr/bin/env python3

if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    m = int(input().strip())
    
    print(pow(a, b))
    print(pow(a, b, m))



# 04. Integers Come In All Sizes
#!/usr/bin/env python3

if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    d = int(input().strip())
    
    print(pow(a, b) + pow(c, d))



# 05. Find Angle MBC
#!/usr/bin/env python3

from math import atan
from math import degrees

if __name__ == "__main__":
    ab = int(input().strip())
    bc = int(input().strip())
    
    print("{}°".format(int(round(degrees(atan(ab/bc))))))



# 06. Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(10**i//9 * i)



# 07. Triangle Quest 2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)**2)


