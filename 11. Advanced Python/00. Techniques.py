# Data Input 
import datetime
a = input("Your Name: ");
b = input("Birth Year: ")

t = datetime.datetime.now(); 
age = t.year - int(b)
print("\nHi " + a + "\nYour Age: " + str(age))


# Print - 1
print("abc")
print('abc')
print("""abc""")
print("ab'c")
print('ab\'c d')
print("16", "London", "2022", sep = "-")
print("Imperial College London\nComputer Science. \nLondon\tEngland")

# Print - 2
a = 99;
b = 123.4567;
c = "London"
print("%d"%a)
print("%d"%b)
print("%X"%a)
print("%10.4o"%a)
print("%0.2f"%b)
print("%0.8f"%b)
print("%10.4e"%b)
print("%10.4g"%b)
print(a,b,c)
print("%d\t%f\t%f"%(a,b,a+b))
print("%c\t%s\t%d"%(c[0], c, a/3))
d = "%s code is %d"%(c, 101)
print(d)


# Print - 3
a = 99;
b = 123.4567;
c = "London"
print("First Value: {}, Second Value: {}".format(a,b))
print("First Value: {0}, Second Value: {1}".format(a,b))
print("Caution! First Value: {1}, Second Value: {0}".format(a,b))
print("First Value: {0}, Second Value: {1:0.2f}".format(a,b))
print("First Value: {0:03d}, Second Value: {1:<10.1f}, Third Value: {2:>10s}".format(a,b,c));
print("{:.2}".format(c))
print("{:^15}".format(c)); 
print("{:+<10}".format(c))


# Print - 3
a = "London";
b = "101"
print(a.center(11,"*"));    # ***London**
print(a.ljust(11, "-"))     # London-----
print(a.rjust(11, ":"));    # :::::London
print(b.zfill(11))          # 00000000101


# For Loop - 1
a = "London"
for i in a:
  print(i)

# For Loop - 2
a = ["Berlin", "Amsterdam", "London", "Madrid", "Miami", "Los Angeles"]
for i in a:
  print(i + " ** ", end = "")
  
# For Loop - 3
for i in range(10):
  print("%d\t"%i, end = "")
print()                     # 0	1	2	3	4	5	6	7	8	9
for i in range(1, 10):
  print("%d\t"%i, end = "")
print()                     # 1	2	3	4	5	6	7	8	9
for i in range(1, 10, 2):
  print("%d\t"%i, end = "")
print()                     # 1	3	5	7	9
for i in range(10, 0, -2):
  print("%d\t"%i, end = "")
print()                     # 10	8	6	4	2



# While Loop - 1
s = 0
while s < 5:
  print(s, "< 5")
  s += 1
else:
  print("loop condition not met.", s,"= 5")
#


# Decision Structure - 1
a = eval(input("Enter a number: "))
if (a > 0):
  print("Positive.")
elif (a < 0):
  print("Negative.")
else:
  print("Zero")


# Decision Structure - 2
a = eval(input("Enter a number: "))
x = -1 * a if (a > 0) else a
print(x)


# Triangle Area - 1
a = float(input("Enter the side length (cm): "))
h = float(input("Enter the height (cm): "))
area = a * h / 2
print("\nTriangle Area (cm²): %0.2f\n"% (area))

# Triangle Area - 2
import math
a = eval(input("Enter the first side (cm): "))
b = eval(input("Enter the second side (cm): "))
angle = eval(input("Enter the angle between (degree): "))
area =  a * b * math.sin(math.radians(angle)) / 2
print("\nTriangle Area (cm²): {:.2f}\n".format(area))


# Odd - Even
a = int(input("Enter an integer: "))
if (a % 2 == 0):
  print("\nInteger entered is even.\n")
else:
    print("\nInteger entered is odd.\n")
#


# Perfect Divisors
a = int(input("Positive Integer: "))
print("%d \nInteger's perfect divisors:"%a)
for i in range(1, a+1):
  if (a%i==0):
    print("%d"%i)
#


# Sums
n = int(input("Enter positive integer: "))
t1 = t2 = t3 = 0
for i in range(1, n+1):
  t1 += i
# instead of loop, t1 = sum(range(1, n+1, 1))

for i in range(1, n+1, 2):
  t2 += i
# instead of loop, t2 = sum(range(1, n+1, 2))

for i in range(2, n+1, 2):
  t3 += i
# instead of loop, t3 = sum(range(2, n+1, 2))
print("\nSum of numbers from 1 to %d:"%n, t1)  
print("\nSum of odd numbers from 1 to %d:"%n, t2)
print("\nSum of numbers from 2 to %d:"%n, t3)


# Combination
f1 = f2 = f3 = 1; n = int(input("n: ")); r = int(input("r: ")) 
for i in range(1, n+1):
  f1 *= i
  if (i <= r):
    f2 *= i
  if (i <= n - r):
    f3 *= i
# Second Way: f1 = math.factorial(n), f2 = math.factorial(r), f3 = math.factorial(n-r)
k = f1 / (f2 * f3)
print("\nResult = %d"% k)

# Combination - 1
import math
print("Combination(n, r)\n"); n = int(input("n: ")); r = int(input("r = "))
f1 = math.factorial(n); f2 = math.factorial(r); f3 = math.factorial(n-r)
k = f1 / (f2 * f3); print("\nCombination(%d, %d) = %d"% (n, r, k))

# Root of First Order Equation
print("ax+b=c"); a = eval(input("a coefficient: "))
b = eval(input("b coefficient: ")); c = eval(input("c coefficient: "))
x = (c-b) / a
print("\n%0.2fx+%0.2f=%0.2f root of the equation: %0.3f\n"%(a,b,c,x))


# Roots of Quadratic Equation 
import math
import cmath
print("Ax^2+Bx+C = 0"); a = eval(input("A = ")); b = eval(input("B = "))
c = eval(input("C = ")); d = b**2-4*a*c
if (d >= 0):
  x1 = (-b-math.sqrt(d))/(2*a); x2 = (-b+math.sqrt(d)) / (2*a)
else:
  x1 = (-b-cmath.sqrt(d))/(2*a); x2 = (-b+cmath.sqrt(d)) / (2*a)
print("\square: "); print(x1, x2, sep = '\n')

# Generating a Quadratic Polynomial 
x1 = eval(input("1. square: ")); x2 = eval(input("2. square: "))
ktop = x1 + x2; kcarp = x1*x2
if (ktop<0):
  print("\nx^2+%0.3fx"%-1*ktop, end='')
else:
  print("\nx^2-%0.3fx"%ktop,end='')
if (kcarp<0):
  print("%0.3f"%kcarp)
else:
  print("+%0.3f"%kcarp)
#


# Piecewise Function
x = eval(input("enter point x: "))
if (x<0):
  y = 1
elif ((0 <= x) & (x <= 2)):
  y = x
elif ((2 <= x) & (x <= 4)):
  y = 3
else:
  y = 4-x
print("At point x = %0.2f, the value of the function = %0.2f\n"%(x, y))

  
  
