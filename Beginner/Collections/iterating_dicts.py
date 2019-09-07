pets = {'name':'Ernie', 'animal':'dog', 'breed':'Pug', 'age':2}

for key, value in pets.items():
    print(key)
    print(value)
	
#only values	
student = {'name': 'Craig', 'major': ['Computer Science', 'Coputer siense'], 'credits': 36}

for val in student.values():
    print(val)

##only keys
	
students = {'name': 'Craig', 'major': 'Computer Science', 'credits': 36}

for key in students.keys():
    print(key)