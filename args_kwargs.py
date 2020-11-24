# args and kwargs

def function(*args):
	print(type(args))
	print("Name is {} age is {} and salary is {}".format(args[0],args[1],args[2]))


list = ["kanay", 21, 70000]
function(*list)
function("kanay",'21',70000)
print()

####################################################################################################
# **kwargs

def function_2(**args):
	print(type(args))
	for key,value in args.items():
		print(key,value)

kwargs = {"name":"kanay","age":21,"salary":80000}
function_2(**kwargs)
function_2(name="kanay",salary="80000",age=21)
print()

####################################################################################################

def function_3(arg,*args,**kwargs):
	print("normal argument ",arg)
	print("variable argument : ", end=' ')
	for arg in args:
		print(arg)

	print("keyworded arguments : ",end = ' ')
	for key,value in kwargs.items():
		print(key,value)

function_3("hello",*list,**kwargs)