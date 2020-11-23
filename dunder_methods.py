class Employee:

	increment = 1.5    #class variable
	
	def __init__(self,name,salary):   #constructor
		self.name = name
		self.salary = salary

	def increase(self): 
		self.salary *= Employee.increment

	@classmethod
	def change_increment(cls,increment):
		cls.increment = increment

	@classmethod
	def from_str(cls, emp_str):
		name, salary = emp_str.split('-')
		return cls(name, salary)

	def __repr__(self):
		return "Employee({},{})".format(self.name, self.salary)

	def __str__(self):
		return "this is an employee class object"

	def __add__(self, other):
		return self.salary + other.salary


obj1 = Employee("kanay",60000)
print(obj1)
obj2 = Employee("kush",80000)



a = 5
print(7+6)
print(a.__add__(6))
print(9+7)
print(obj1 + obj2)