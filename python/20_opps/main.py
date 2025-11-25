class Student:
    college_name = "VNSGU"
    count = 0

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        Student.count += 1

    def get_cgpa(self):
        return self.cgpa

    @classmethod
    def college_name_print(cls):
        print(f"College name is = {cls.college_name}")

    @classmethod
    def get_count(cls):
        print(f"Total student is => {cls.count}")

    @staticmethod
    def static_method_print(totalMarks, totalFrom):
        print(f"Marks is => {(totalMarks*100)/totalFrom}")


s1 = Student("meet", 7.1)
print(s1.name, s1.cgpa)
s2 = Student("arjun", 9)
print(s2.name, s2.cgpa)
s3 = Student("mitul", 8)
print(s3.name, s3.cgpa)
s4 = Student("hardik", 7.5)
print(s4.name, s4.cgpa)
s5 = Student("hardik", 7.5)
print(s5.name, s5.cgpa)

print(f"{s1.name} has cgpa = {s1.get_cgpa()}")

# class method
s1.college_name_print()
Student.college_name_print()
Student.get_count()
# call static method
s1.static_method_print(650, 700)

# In calss if we have same variable in class and in instance then if you try to access from class object then instance variable will be in high priority and if you access direct using class then the class variable is in high priority.

# There are two method in class static methos and classmethod => assume you have defined a method in class so that method will be accessable only when you create a class object so to make it global like to make it you can use direct using class without creating a object then you have to use a key word just before the method defination =>  @classmethod. And another method in static which is use when the function is static there is no dynamic behaviour in that function or methog so you can use this method just before method defination =>@staticmethod


# 4 piller of opps

# 1. Encapsulation
# 2. abstraction
# 3. Inheritance
# 4. Polymorphism
