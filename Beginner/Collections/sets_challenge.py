COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(corses):
    new_list = []
    for key, value in COURSES.items():
        if value.intersection(corses):
            new_list.append(key)
    return new_list      


def covers_all(all_topics):
    course_list = []
    for key, value in COURSES.items():
        if all_topics.issubset(value):
            course_list.append(key)
    # print('course list is: {}'.format(course_list))
    return course_list
