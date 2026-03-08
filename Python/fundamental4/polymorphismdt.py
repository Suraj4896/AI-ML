class Employee:
    def get_designation(self):
        print('employee')

#duck typing
class Teacher:
    def get_designation(self):
        print('teacher') 

t1 = Teacher()
t1.get_designation()