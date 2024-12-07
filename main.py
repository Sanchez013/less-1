class Student:
    def __init__(self, name, age ):
        self.name = name 
        self.age = age 

    def greeting(self):
        print(f"hello, I am {self.name}")

    def grow_up (self):
        self.age = self.age + 1

    def print_age(self):
        print(f"age - {self.age}")


oleksandr_student = Student(name = "Oleksandr", age = 15)
oleksandr_student.greeting()

matvii_student = Student(name = "Matvii", age = 14)
matvii_student.greeting()

