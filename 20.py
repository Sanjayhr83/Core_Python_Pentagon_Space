#has-a relationship

#composed object
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

class OS:
    def __init__(self):
        self.os="IOS 26.4"
        print("OS is updating")
    def update(self):
        print("OS is updated")
class Phone:
    def name(self):
        self.pname="Iphone 17 pro max"
        print("My new phone is {}".format(self.pname))
        self.oss=OS()
p=Phone()
p.name()
print(p.oss.os)
p.oss.update()

class Animal:
    def __init__(self):
        self.name="animal"
    def eat(self):
        print("eating")
class dog:
    def __init__(self):
        self.name="dog"
    def eated(self):
        print("dog eating pedigree")
        self.c=Animal()
d=dog()
d.eated()
print(d.name)
d.c.eat()
print(d.c.name)
del d
print(d.name)

class PS:
    def __init__(self):
        self.batch="jan 25th"
    def head(self):
        print("Shashank sir is python head")
class abhi:
    def __init__(self):
        self.comb="SD"
    def course(self):
        self.ins="TAP"
        print("Java full stack is course")
        self.p=PS()

a1=abhi()
print(a1.comb)
a1.course()
print(a1.ins)
a1.p.head()
print(a1.p.batch)
del a1
a1.course()


#aggregate object
class charger:
    def __init__(self,name):
        self.cname=name
    def getcharger(self):
        print("charger is  plugged in")

class mobile:
    def __init__(self,name):
        self.mname=name
        self.c=""
    def hasmobile(self,p):
        self.c=p
m1=mobile("IQOO")
c1=charger("Flash(C_pin)")
m1.hasmobile(c1)
print(m1.mname)
m1.c.getcharger()
del m1
print(c1.cname)
c1.getcharger()

class Animal:
    def __init__(self,name):
        self.aname=name
    def action(self):
        print("Animal are mammal,reptiles,birds,amphibians")
class lion:
    def __init__(self,name):
        self.lname=name
        self.z=""
    def attitude(self,x):
        print("Lion is a king and mammal")
        self.z=x
a1=Animal("Tiger")
l1=lion("Simba")
l1.attitude(a1)
print(l1.z.aname)
l1.z.action()
print(l1.lname)
del l1
a1.action()
print(a1.aname)

class bunk:
    def __init__(self,name):
        self.bname=name
    def quality(self):
        print(f"{self.bname} is top quality")
class bike:
    def __init__(self,name):
        self.biname=name
        self.d=""
    def milage(self,e):
        print(f"{self.biname } is heavy bike")
        self.d=e
b=bunk("HP")
f=bike("Bajaj")
f.milage(b)
print(f.d.bname)
print(f.biname)
f.d.quality()
del f
b.quality()
print(b.bname)

class PS:
    def __init__(self):
        self.batch="jan 25th"
    def head(self):
        print("Shashank sir is python head")
class abhi:
    def __init__(self):
        self.comb="SD"
        self.c=""
    def course(self,P):
        self.ins="TAP"
        print("Java full stack is course")
        self.c=P
a1=abhi()
p1=PS()
a1.course(p1)
print(a1.ins)
a1.c.head()
print(a1.c.batch)
del a1
p1.head()


#combining of both composition and aggregation
class heart:
    def __init__(self):
        self.status="empty"
    def heartattack(self):
        self.health="good"
        print("Heart is pumping")
class cycle:
    def __init__(self):
        self.cname="Atlos"
    def buycycle(self):
        print("Person buy new cycle")
class person:
    def __init__(self,name):
        self.pname=name
        self.c=cycle()
        self.z=""
    def hasperson(self,P):
        self.z=P
p1=person("Ram")
h1=heart()
p1.hasperson(h1)
print(p1.pname)
p1.c.buycycle()
print(p1.c.cname)
print(p1.z.status)
p1.z.heartattack()
print(p1.z.health)
del p1
print(h1.status)
print(p1.c.cname)