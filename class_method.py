class Employee:

	increment = 1.5
	no_of_employees = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.no_of_employees += 1

	def increase(self):
		self.salary *= Employee.increment

	@classmethod
	def change_increment(cls,increment):
		cls.increment = increment

	@classmethod
	def from_str(cls, emp_str):
		name, salary = emp_str.split('-')
		return cls(name, salary)

	@staticmethod
	def about():
		return "this is a Employee class"

obj = Employee("kanay",60000)
print(obj.salary)

obj.increase()
print(obj.salary)

obj.change_increment(2)
obj.increase()
print(obj.salary)

print(Employee.no_of_employees)

obj2 = Employee("kush",70000)
print(Employee.no_of_employees)

#############################################################################################
# class method as alternative constructor


obj3 = Employee.from_str("subham-90000")

print(obj3.name)
print(obj3.salary)

#############################################################################################
# static method
print(Employee.about())