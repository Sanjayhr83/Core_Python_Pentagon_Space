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
