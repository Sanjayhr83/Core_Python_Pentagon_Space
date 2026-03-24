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