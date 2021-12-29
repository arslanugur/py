# Chapter : Basic concepts
# Lesson : Quotient & remainder
# Code Practice : Sorting Out

# Explanation
# We need to pack 142 toys in boxes. Each box holds 15 toys.

# Task
# Write a program to calculate and output how many toys will be left after packing.

# Hint
# Find the remainder from dividing 142 and 15.

# Note: Use the modulo operator (%) to get the remainder.

# OOP solution just for training

# Code:
class CrossMultiplier():
	"""
	This class performs
	cross-multiplication.
	c  -->  a
	x  -->  b
	x = b * c / a
	The goal is to find x.
	"""
	def __init__(self, a, b, s='/', c=1):
		self.a = a
		self.b = b
		self.c = c
		self.s = s
		self.n = self.b * self.c
		if self.s == '/':
			print(self.cross_multip()) # this outputs the result directly.
		elif self.s == '//':
			self.quotient() # initialization of an object calls quotient() method, which performs the calculation. Its result can be displayed thanks to show() method.
		elif self.s == '%':
			self.remainder() # same here, need to use show() method.
	def cross_multip(self):
		self.x = self.n / self.a
		return self.x
	def quotient(self):
		self.x = self.n // self.a
		return self.x
	def remainder(self):
		self.x = self.n % self.a
		return self.x
	def show(self):
		print(self.x)
	
t = CrossMultiplier(15,142,'%')
t.show()
# Try this too :
#t = CrossMultiplier(15,142,)
#t.show()


  
