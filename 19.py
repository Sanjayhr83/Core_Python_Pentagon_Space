#Abstraction
"""
Abstraction means:
👉 Hiding internal details and showing only essential features
You use something without knowing how it works internally.

🧠 Real-Life Examples
🚗 Driving a car → You use steering & pedals, not engine logic
📱 Mobile phone → You tap apps, not internal code
🏧 ATM → You withdraw money without knowing backend process
🧾 Abstraction in Python

In Python, abstraction is implemented using:

Abstract Classes
Abstract Methods

👉 Using the built-in module:
from abc import ABC, abstractmethod
"""

"""
🔥 Abstraction vs Encapsulation
Feature	         Abstraction         Encapsulation
Focus	    Hiding complexity	    Hiding data
How	        Abstract classes	    Private variables
Example	    abstractmethod	        __variable
"""

from abc import ABC, abstractmethod

class Animal(ABC):   #abstract class
    @abstractmethod
    def sound(self):    #abstract method
        pass
class Lion(Animal):
    def sound(self):
        print("Lion is roaring...")
l=Lion()
l.sound()

from abc import ABC, abstractmethod
class Vehicle(ABC):   # Abstract class
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")

c = Car()
b = Bike()
c.start()
b.start()

# Payment System (Real-World)
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")
class UPI(Payment):
    def pay(self):
        print("Paid using UPI")
def makePayment(method):
    method.pay()

makePayment(CreditCard())
makePayment(UPI())

# Shape Area
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class reactangle(shape):
    def area(self):
        print("Area = length X breadth")
class circle(shape):
    def area(self):
        print("Area = πr²")
c=circle()
r=reactangle()
c.area()
r.area()

# Shape Area using for loop
from abc import ABC, abstractmethod
print("Shape Area using for loop")
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area = length × breadth")
class Circle(Shape):
    def area(self):
        print("Area = πr²")

shapes = [Rectangle(), Circle()]

for s in shapes:
    s.area()

from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON")
    def turn_off(self):
        print("TV is OFF")
class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON")
    def turn_off(self):
        print("AC is OFF")
devices = [TV(), AC()]

for d in devices:
    d.turn_on()
    d.turn_off()

# Notification System (Very Useful in Apps)
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):
        print("Sending Email")

class SMS(Notification):
    def send(self):
        print("Sending SMS")

class WhatsApp(Notification):
    def send(self):
        print("Sending WhatsApp Message")

def notify(obj):
    obj.send()

notify(Email())
notify(SMS())
notify(WhatsApp())

# Employee Salary System
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def calculate_salary(self):
        print("Monthly salary: 50000")

class PartTime(Employee):
    def calculate_salary(self):
        print("Hourly salary: 500 per hour")

emps = [FullTime(), PartTime()]

for e in emps:
    e.calculate_salary()


# Abstract Class with Partial Implementation
from abc import ABC, abstractmethod

class Vehicle(ABC):

    def fuel_type(self):   # normal method
        print("Uses fuel")

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

c = Car()
c.fuel_type()
c.start()

#File Handling System (Advanced Concept)
from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

class TextFile(FileHandler):
    def read(self):
        print("Reading text file")

class PDFFile(FileHandler):
    def read(self):
        print("Reading PDF file")

files = [TextFile(), PDFFile()]

for f in files:
    f.read()

