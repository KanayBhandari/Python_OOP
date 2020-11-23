# Object oriented programming in python (class object and members)

class Test:
	def fun(self):
		print("programming is fun")

# Driver Code
a = Test()
a.fun()

######################################################################################################
# The __init__ method

class Person:
	def __init__(self,name):
		self.name = name

	def say_hi(self):
		print("Hello my name is : ",self.name)

p = Person("Kanay")
p.say_hi()

######################################################################################################
# Class and Instance Variable

class CSStudent:
	# Class Variable
	stream = "CSE"

	def __init__(self,roll):
		# Instance Variable
		self.roll = roll

	def set_address(self,address):
		# Instance Variable
		self.address = address

	def get_address(self):
		return self.address

a = CSStudent(1)
b = CSStudent(2)

print(a.stream)
print(b.stream)
print(CSStudent.stream)
a.set_address("haldwani, Uttarakhand")
print(a.get_address())

######################################################################################################
# Create an empty class

class Test:
	pass