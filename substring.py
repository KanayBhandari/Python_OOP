# Count the number of substring match
# 1. Using startswith()

# def count_substring(string,sub_string):
# 	count = 0
# 	for i in range(len(string)):
# 		if string[i:].startswith(sub_string):
# 			count += 1
# 	return count

# if __name__ == '__main__':
# 	string = input()
# 	sub_string = input()
# 	result = count_substring(string,sub_string)
# 	print(result)


# 2. Using find()
def count_substring(string,sub_string):
	count = 0
	while sub_string in string:
		count += 1
		i = string.find(sub_string)
		string = string[i+1:]
	return count

if __name__ == '__main__':
	string = input()
	sub_string = input()
	result = count_substring(string,sub_string)
	print(result)