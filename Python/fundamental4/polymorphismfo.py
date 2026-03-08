class Employee:
    def get_designation(self):
        print('employee')

#function overriding 
class Teacher(Employee):
    def get_designation(self):
        print('teacher') 

t1 = Teacher()
t1.get_designation()