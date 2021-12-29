# Chapter : Basic concepts
# Lesson : Simple Operations
# Code Practice : Brain Freeze!

# Explanation:
# Today is a holiday at the children's camp, so all the children will be served ice cream.
# There are 68 children in the group, and each child should get 2 scoops of ice cream.

# Task
# Write a program to calculate and output the total number of ice cream scoops we need. 

# Note: Use the multiplication operator * inside the print() function.

# Code:
# OOP solution just for fun !
class Camp():
	name = "Tommy's holiday camp"
	lat = None
	lon = None
	def __init__(self):
		self.children = 0
		self.nb_scoop = 0
	def add_children(self, other):
		self.children += other.nb
		other.camp = Camp.name
	def is_holiday(self, arg):
		if arg == 1 or arg[0].lower() == 'y':
			self.nb_scoop = 2
			IceCream.camp = Camp.name
			scoops_given = IceCream.give_icecream(self, self.nb_scoop, self.children)
			return scoops_given[0]		
	
class Children():
	def __init__(self, nb):
		self.nb = nb
		self.camp = None
		
class IceCream():
	stock = 500 #nb of scoops in stock
	flavour = "water"
	def __init__(self):
		self.camp = None
	def give_icecream(self, nb_scoop, children):
		self.ice_cream = nb_scoop * children
		IceCream.stock -= self.ice_cream
		return self.ice_cream, IceCream.stock
	def put_icecream(self, other):
		IceCream.stock += other.nb_scoop
		return IceCream.stock

children = Children(68)
camp = Camp()
camp.add_children(children)
ice_cream_given = camp.is_holiday(True)
#print(camp.children)
#print(children.camp)
#print(camp.nb_scoop)
print(ice_cream_given)


