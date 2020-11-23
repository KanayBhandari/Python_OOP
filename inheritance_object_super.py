# Inheritance, examples of object, issubclass and super

class Person(object):
	def __init__(self,name):
		self.name = name

	def getName(self):
		return self.name

	def isEmployee(self):
		return False

class Employee(Person):

	def isEmployee(self):
		return True

emp = Person("kanay1")
print(emp.getName(), emp.isEmployee())

emp = Employee("kanay2")
print(emp.getName(), emp.isEmployee())

######################################################################################################
# How to check if a class is subclass of another?

class Base:
	pass

class Derived(Base):
	pass

print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d = Derived()
b = Base()

print(isinstance(b,Derived))
print(isinstance(d,Derived))
print(isinstance(d,Base))

######################################################################################################
# Multiple Inheritance in python

class Base1:
	def __init__(self):
		self.name1 = "kanay1"
		print("Base1")


class Base2:
	def __init__(self):
		self.name2 = "kanay2"
		print("Base2")


class Derived(Base1,Base2):
	def __init__(self):
		# Calling constructor of Base1 and Base2 class
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printName(self):
		print(self.name1,self.name2)

b = Derived()
b.printName()

######################################################################################################
# How to access parent members in a subclass
# 1. Using parent class name

class Base:
	def __init__(self,x):
		self.x = x

class Derived(Base):
	def __init__(self,x,y):
		Base.x = x
		self.y = y

	def printXY(self):
		# print(self.x,self.y) will also work
		print(Base.x,self.y)

d = Derived(10,20)
d.printXY()


# 2. Using super()

class Base:
	def __init__(self,x):
		self.x = x

class Derived(Base):
	def __init__(self,x,y):
		super(Derived,self).__init__(x)
		self.y = y

	def printXY(self):
		print(self.x,self.y)

d = Derived(100,200)
d.printXY()

######################################################################################################

class A:
	def __init__(self,a):
		self.num = a
	def doubleup(self):
		self.num *= 2

class B(A):
	def __init__(self,a):
		A.__init__(self,a)
	def tripleup(self):
		self.num *= 3

b = B(10)
b.doubleup()
print(b.num)
b.tripleup()
print(b.num)

######################################################################################################
# Python Inheritance
class Person:
	def __init__(self,name,idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

class Employee(Person):
	def __init__(self,name,idnumber,salary,post):
		self.salary = salary
		self.post = post
		Person.__init__(self,name,idnumber)


a = Employee("kanay",1,'60000',"developer")
a.display()

######################################################################################################
# Multi-Level inheritance

class Base:
	def __init__(self,name):
		self.name = name

	def getName(self):
		return self.name

class Child(Base):
	def __init__(self,name,age):
		Base.__init__(self,name)
		self.age = age

	def getAge(self):
		return self.age


class GrandChild(Child):
	def __init__(self,name,age,address):
		Child.__init__(self,name,age)
		self.address = address

	def getAddress(self):
		return self.address

g = GrandChild("kanay",21,"haldwani")
print(g.getName(),g.getAge(),g.getAddress())

######################################################################################################
# Python program to demonstrate private members of parent class

class C:
	def __init__(self):
		self.c = 20
		# d is private instance variable
		self.__d = 10

class D(C):
	def __init__(self):
		self.e = 60
		C.__init__(self)

obj = D()
print(obj.c)
print(obj.e)
print(obj.d)