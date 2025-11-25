# there are two things
# 1. function overriding (happen when there is inheritence like if there is a function in parent class and in child there is a same name function then function overriding comes into the picture)
# 2. duck typing


# function overriding (So in this case it will override and call last herited class function)
class Employee:
    def get_designation(self):
        print("Designation==Employee")


class Teacher(Employee):
    def get_designation(self):
        print("Designation==Teacher")


t = Teacher()
t.get_designation()


# duck typing (same named function but in defference class no inheritance there)
class Teacher1():
    def get_designation(self):
        print("Designation==Teacher1")


class Accountant():
    def get_designation(self):
        print("Designation==Account")


t1 = Teacher1()
t1.get_designation()
acc = Accountant()
acc.get_designation()
