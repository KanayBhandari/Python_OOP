class Employee:

	increment = 1.5
	no_of_employees = 0

	def __init__(self,fname,lname,salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary
		Employee.no_of_employees += 1

	def increase(self):
		self.salary *= Employee.increment

	@property
	def email(self):
		if self.fname == None:
			return "email not set"
		else:
			return self.fname + '.' + self.lname + '@email.com'

	@email.setter
	def email(self, given_email):
		email_list = given_email.split('@')[0].split('.')
		self.fname = email_list[0]
		self.lname = email_list[1]

	@email.deleter
	def email(self):
		self.fname = None
		self.lname = None

	@classmethod
	def change_increment(cls,increment):
		cls.increment = increment

	@classmethod
	def from_str(cls, emp_str):
		name, salary = emp_str.split('-')
		return cls(name, salary)


if __name__ == "__main__":
	kanay = Employee("kanay","bhandari",80000)
	kush = Employee("kush","bhandari",90000)

	print(kanay.email)
	print(kush.email)

	kanay.email = "karan.bhandari@email.com"
	print(kanay.email)

	del kanay.email
	print(kanay.email)