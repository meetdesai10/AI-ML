# wrapping data & function into single unit that is called encapsulation
# data hiding
# there are three type of attribute
# protected attribute
# self._balance => single _ mean it is protected => can be accessable
# private attribute
# self.__balance => double __ mean it is private => can not be accessable. we can give using getter and setter
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):  # getter
        return self.__balance

    def set_balace(self, newBalnce):  # setter
        self.__balance = newBalnce


acc1 = BankAccount("Meet", 100_000)
print(acc1.name, acc1.get_balance())
acc1.set_balace(200_000)
print(acc1.name, acc1.get_balance())
# we can private access like this there is no true private things in python its just a concept for the developer to know which is private so we dont use outside.
print(acc1.name, acc1._BankAccount__balance)
