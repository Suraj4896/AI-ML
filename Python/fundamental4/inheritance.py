class Employee:
    start_time = '10am'
    end_time = '6pm'

class A:
    def __init__(self, salary):
        self.salary = salary
        
class B:
    def __init__(self, gpa):
        self.gpa = gpa


#multiple inheritance
class C(A, B):
    def __int__(self, salary, gpa, name):
        super().__init__(salary) #if super then no need of self
        B.__init__(self, gpa) #if class name, pass self
        self.name = name
        
        
#inheritance
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

#multilevel inherit.
class Accountant(Teacher):
    def __init__(self, salary, subject):
        super().__init__(subject)
        self.salary = salary


t1 = Teacher('Math')
a1 = Accountant(10_000, 'Math')
print(t1.subject, t1.start_time, t1.end_time)
        