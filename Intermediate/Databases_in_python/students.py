#acts like a local database, good exampple for unsderstanding peewee and db queries

from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

    
    
students = [
    {'username' : 'oskar',
     'points' : 4888},
    {'username' : 'bb4',
     'points' : 467},
    {'username' : 'tori',
     'points' : 48432},
    {'username' : 'pelok',
     'points' : 1000},
    ]   

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                      points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()
            
        

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()  ##last get() gets only the last record otherwie ti just gets the higest score student
    return student
    
    
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print('Our top student is: {0.username}.'.format(top_student()))