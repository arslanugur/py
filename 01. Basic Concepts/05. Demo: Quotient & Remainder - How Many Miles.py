# Example: Quotient
# Calculate and output the number of miles in 1000 kilometers.

# Hint:
# One mile is 1.6 kilometers, so find the quotient of 1000 and 1.6.
# Use the floor division operator //.

# Code:
print(1000 // 1.6)


# Second Way
def to_miles(km):
  miles= km / 1.609
  return miles;

km=float(input())
miles= to_miles(km)
print(str(miles)+ " miles")


