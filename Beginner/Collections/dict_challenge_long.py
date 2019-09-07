import operator
# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

#counting the number of teachers
def num_teachers(dic):
    counter = 0
    for key in dic.keys():
        counter += 1    
    return counter

#counting the number of courses
def num_courses(dic):
	counter = 0
	for val in dic.values():
		if type(val) is list:
			counter += len(val)	
		else:
			counter += 1
	return counter

#creates list with just courses
def courses(dic):
    courses = []
    for val in dic.values():
        courses.extend(val)
    return courses

#teachers with most courses
def most_courses(dic):
    teachers = {}
    for key, val in dic.items():
        if type(val) is list:
            teachers[key] = len(val)
    winner = max(teachers.items(), key=operator.itemgetter(1))[0]
        
    return winner

#stats should return a list of lists where the first item in each inner list is the teacher's name 
#and the second item is the number of courses that teacher has. For example,
#it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]#
def stats(dic):
    stats = [] 
    for key, val in dic.items():
        if type(val) is list:
            courses = len(val)
            stats.append([key, courses])
        else:
            stats.append([key, 1])
        
    return stats
    
        
	
print(stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', 'jsdkfj'], 'Kenneth Love': ['Python Basics', 'Python Collections']}))