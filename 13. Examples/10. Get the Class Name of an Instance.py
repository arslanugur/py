# To get the class name of an instance

# Example 1: Using __class__.__name__
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)

# Output: Vehicle

# __class__ is the attribute of the class to which it is associated and __name__ is a special variable in Python. Its functionality depends on where it is used.
#   - Create an object v of class Vehicle().
#   - Print the name of the class using __class__.__name__.



# Example 2: Using type() and __name__ attribute
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(type(v).__name__)

# Output: Vehicle

# Using attribute __name__ with type(), you can get the class name of an instance/object as shown in the example above. 
# type() gives the class of object v and __name__ gives the class name.


