# tyes of inheritance
# 1. single level inheritance => only single level like there is only one is using the main class as a heritance
# 2. multi level inheritance => use multi level like if there is a five classes then 5 is using 4 4 is using 3 3 is using 2 2 using 1 like this. Like a hierarchy
# 3. multiple level inheritance => it means like there is a class named employee and there are another two class 1. staff 2. accountant when both use same class called employee as a inheritance thenit call multiple inheritance not like a hierarchy.
class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_end_time(self, new_time):
        self.end_time = new_time

# multi level inheritance


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary


t1 = Teacher("Math")
t1.change_end_time("1pm")
print(t1.subject, t1.start_time, t1.end_time)

staff1 = AdminStaff("manager")
print(staff1.role, staff1.start_time, staff1.end_time)

acc1 = Accountant(25_000, "CA")
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


# multi level inheritance
class Teacher1:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(Teacher1, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name


ta1 = TA(15_000, 9.3, "meet")
print(ta1.name, ta1.gpa, ta1.salary)
