def stringcases(string):
    formats = string.upper(), string.lower(), string.title(), string[::-1]
    return formats
    

print(stringcases("aabits"))
    
# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(iter1, iter2):
    first = []
    second = []
    li = []
    for it1 in iter1:
        first.append(it1)
    for it2 in iter2:
        second.append(it2)
    for index, item in enumerate(first):
        li.append((first[index], second[index]))

    return li
		
    
	
print(combo([1, 2, 3], 'abc'))