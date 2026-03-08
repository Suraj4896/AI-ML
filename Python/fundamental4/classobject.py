class Student:
    #class attribute
    college_name = 'NITW'

    #constructor / instance attribute
    def __init__(self, name, cgpa): #parameterized constructor
        self.name = name
        self.cgpa = cgpa
        print('constructor is called')

    #instance method
    def get_info(self):
        print(f'{self.name} is from {self.college_name} has cgpa {self.cgpa}')
    
    #class method
    @classmethod
    def get_college(cls):
        print(f'college name is {cls.college_name}')

    #static method
    @staticmethod
    def cal_discount(price, disc):
        final_price = price - (disc * price / 100)
        print(f'final price is {final_price}')


std1 = Student('suraj', 9.5)
print(std1.name)
print(std1.cgpa)
print(std1.college_name)
print(Student.college_name)
std1.get_info()
Student.get_college()
