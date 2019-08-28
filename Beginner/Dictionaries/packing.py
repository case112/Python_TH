#example1

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)
    
print_teacher(name='Ashley', job='Instructor', topic='Python')

#example2

def print_teachers(**kwargs):
	for key, value in kwargs.items():
		print(f'{key}: {value}')
      

print_teachers(name='Ashley', job='Instructor', topic='Python', second_topic='javascript')


#example3

teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)
	
print_teacher(**teacher)

