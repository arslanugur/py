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














  
