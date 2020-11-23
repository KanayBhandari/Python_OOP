# Data hiding and object printing

class MyClass:
	# hidden member of MyClass
	__hidden_Variable = 0

	def add(self,increment):
		self.__hidden_Variable += increment
		print(self.__hidden_Variable)

m = MyClass()
m.add(3)
m.add(6)

# this line will cause error
# print(m.__hidden_Variable)

#############################################################################################
# Accessing hidden value by tricky syntax

class MyClass:
	__hidden_Variable = 5

myObject = MyClass()
print(myObject._MyClass__hidden_Variable)


#############################################################################################
# Printing Objects

class Test:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __repr__(self):
		return "test a : %s b : %s" %(self.a, self.b)

	def __str__(self):
		return "From str method of test a : %s b : %s" % (self.a, self.b)

t = Test(12,45)
print(t)
print([t])

#############################################################################################
# If no __str__ method is defined print t ( or print str(t)  )uses __repr__

class Test:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __repr__(self):
		return "Test a : %s b : %s" %(self.a, self.b)

t = Test(66, 54)
print(t)

#############################################################################################
# If no __repr__ method is defined default is used

class Test:
	def __init__(self,a,b):
		self.a = a
		self.b = b

t = Test(456,432)
print(t)