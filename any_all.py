# Use of any and all in python
# any and all are two biltins provided in python for succesive And/Or

print(any(['True','False','False'])) # True
print(any([False,False,False])) # False
print(any((False,False,True))) # True
print(any({1:"kanay"})) # True
print(any({})) # False


# Use of all
print(all([])) # True
print(all([True,True])) # True
print(all([True,True,False])) # False
print(all(())) # True


print(any([i for i in range(3)]))
