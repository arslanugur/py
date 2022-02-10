# Object Oriented Examples
# Example: To differentiate between type() and isinstance()

# Difference between type() and instance()

# Let's understand the difference between type() and instance() with the example code below.
class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):
    def area(self):
        pass

obj_polygon = Polygon()
obj_triangle = Triangle()

print(type(obj_triangle) == Triangle)   	# True
print(type(obj_triangle) == Polygon)    	# False

print(isinstance(obj_polygon, Polygon)) 	# True
print(isinstance(obj_triangle, Polygon))	# True


# In the above example, we see that type() cannot distinguish whether an instance of a class is somehow related to the base class. 
# In our case, although obj_triangle is an instance of child class Triangle, it is inherited from the base class Polygon. 
# If you want to relate the object of a child class with the base class, you can achieve this with instance().


