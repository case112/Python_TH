#I need you to create a new function for me.
#This one will be named sillycase and it'll take a single string as an argument.
#sillycase should return the same string but the first half should be lowercased and the second half should be uppercased. For example, with the string #\"Treehouse\", sillycase would return \"treeHOUSE\".
#Don't worry about rounding your halves, but remember that indexes should be integers. You'll want to use the int() function or integer division, //."

def sillycase(string):
	
	length = len(string)
	lower = length // 2
	upper = length - (length //2)
	first = string[:lower:]
	if upper != lower:
		upper -= 1
	second = string[upper::]
	new_string = first.lower() + second.upper()
	
	print(length)
	print(lower)
	print(upper)
	print(first)
	print(second)
	
	return new_string
	
	
print(sillycase("Treehouse"))