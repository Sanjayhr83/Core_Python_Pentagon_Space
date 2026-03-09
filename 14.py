#oops(object oriented programming structure or system)
#encapsulatioin
class book:
    def __init__(self,page):
        self.__pages=page

    def setter(self,val):
        if val>0:
            self.__pages=val

    def getter(self):
        return self.__pages

b=book(100)
res1=b.getter()
print(res1)
b.setter(200)
res2=b.getter()
print(res2)
b.setter(-99)
res3=b.getter()
print(res3)

#identifiers(public,_protected,__private)
#Protected Access Modifier
class Student:
    def __init__(self):
        self._marks = 85
s = Student()
print(s._marks)

#Private Access Modifier
class Student:
    def __init__(self):
        self.__marks = 90
    def get_marks(self):
        return self.__marks
s = Student()
print(s.get_marks())

#simple ATM example using encapsulation
class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)