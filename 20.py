#has-a relationship
class Radio:
    def turnon(self,x):
        if x==1:
            print("Radio is turned on")
        else:
            print("Radio is turned off")
class Car:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.r=Radio()
z=Car(10,120)
print(z.min)
print(z.max)
z.r.turnon(1)
z.r.turnon(0)


class Solution:
    def dis(self):
        print("solution is not good")
    def disp(self):
        print("solution is good")
class prob:
    def __init__(self):
        self.task="01"
        self.task2="02"
        self.s=Solution()
z=prob()
print(z.task)
print(z.task2)
z.s.disp()
z.s.disp()

class A:
    def dis(self):
        print("I'm Class A ")
        print("And i am base class")
class C(A):
    def dis(self):
        print("I'm Class C ")
        self.a=A()

c=C()
c.dis()
c.a.dis()

#Composed object
class OS:
    def __init__(self):
        self.status=True
        print("OS is ready")
    def getos(self):
        print("OS is installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=OS()
        print("Mobile is ready")
        print("with os installed")
m=Mobile("Nokia")
print(m.mname)
print(m.o.status)
m.o.getos()
del m
print(m.o.status)

class Petrolbank:
    def __init__(self):
        print("The petrolbank name HP")
    def price(self):
        print("Petrol $104 per liter \nDiesel $94 per liter")
class Bike:
    def drive(self):
        print("The bike is fill with Petrol")
    def stop(self):
        print("Bike is stop because Petrol is enough")
        self.z=Petrolbank()
a=Bike()
a.drive()
a.stop()
a.z.price()