# **kwargs takes arguments and packs them into dictionary

#name=None does not save new keyword argument
def packer(name=None, **kwargs):
	print(kwargs)


def unpacker(first_name=None, last_name=None):
	if first_name and last_name:
		print("Hi, {} {} !".format(first_name, last_name))
	else:
		print("Hi no name!")
		
		
		
packer(name='Ashley', job='Instructor', topic='Python', second_topic='javascript')		
unpacker(**{"last_name" : 'Ash', "first_name" : 'Jacks'})

course_minutes = {"course1" : 345, "course2" : 422, "course3" : 35, "course4" : 3325,}

for course, minutes in course_minutes.items():
	print("{} is {} minutes long".format(course, minutes))