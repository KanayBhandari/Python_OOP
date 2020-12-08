# Different ways of converting a string input into a integer list
# 1. Using map() function which takes two argument first a function and second a iterable
# 2. Using list comprehensions
# 3. Using a for loop and getting a integer value stored in a variable and then appending it to the end 
#    of an empty list

raw_input = input()
input_list = raw_input.split(' ') # it will return the list of strings
print(input_list)

integer_list = list(map(int,input_list)) # it will return the list of integers
integer_list1 = [int(x) for x in input_list] # it will return the list of integers

integer_list2 = [] # it will create an empty list
for i in range(len(input_list)):
	a = int(input_list[i])
	integer_list2.append(a) # it will return the list of integers

print(integer_list)
print(integer_list1)
print(integer_list2)



# Precision handling in python
# 1. Using %
# 2. Using format()
# 3. Using round(x,n)

a = 10.2347
print(a)
print("{0:.2f}".format(a))
print("%.2f"%a)
print(round(a,2))