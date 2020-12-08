######################################################################################
# Text wrap

def wrap(string,max_width):
	s = ''
	for i in range(0,len(string),max_width):
		s = s + string[i:i+max_width] + '\n'
	return s

def wrap1(string,max_width):
	s = ''
	s = '\n'.join(string[i:i+max_width] for i in range(0,len(string),max_width))
	return s

if __name__ == '__main__':
	string, max_width = input(), int(input())
	result = wrap(string,max_width)
	result1 = wrap1(string,max_width)
	print(result)
	print()
	print(result1)



# ######################################################################################
# def print_formatted(number):
#     width = len("{0:b}".format(number))
#     print(width)
#     for i in range(1,number+1):
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))
#     # your code goes here

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)