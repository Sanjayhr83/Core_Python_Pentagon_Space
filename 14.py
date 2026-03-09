#oops(object oriented programming structure or system)
#encapsulatioin
class book:
    def __init__(self,page):
        self.__pages=page

    def setter(self,val):   #setter method: to set value using particular condition
        if val>0:
            self.__pages=val

    def getter(self):   #getter is used to get a value from the class
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


#example for setter and getter
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student("Anita", 20)
print("Age:", student.get_age())  # Accessing age with getter
student.set_age(21)  # Modifying age with setter
print("Updated Age:", student.get_age())


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