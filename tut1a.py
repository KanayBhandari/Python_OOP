import os

def employee():
	print("this is the employee function")

def list():
	print(os.getcwd())
	print(os.listdir('/'))


print(__name__)

if __name__ == "__main__":
	employee()
	list()