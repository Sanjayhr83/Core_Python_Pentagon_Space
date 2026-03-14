#inheritance(it is a mechanism which allows us to inherit the property and behaviour of one class to another class)
class parent:
    def __init__(self):
        self.a=10

class child(parent):  #both class connected
    def __init__(self):
        parent.__init__(self)   #both constructors connected
        self.b=20
c=child()
print(c.b)
print(c.a)


class A:    #act as only parent
    def __init__(self):
        self.a=100

class B:    #act as both parent and child
    def __init__(self):
        A.__init__(self)
        self.b=200

class C:    #act as only child
    def __init__(self):
        B.__init__(self)
        self.c=300
z=C()
print(z.c)
print(z.b)
print(z.a)

#super() method:
class Parent:
    def show(self):
        print("This is parent method")
class Child(Parent):
    def display(self):
        super().show()
        print("This is child method")
c = Child()
c.display()
#example for super() with constructor
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
s = Student("Sanjay", 21)
print(s.name, s.age)


#without follow impletementation of inheritance
class Passengerplane:
    def takeoff(self):
        print("passengerplane is taking off")
    def fly(self):
        print("passengerplane is flying")
    def land(self):
        print("passengerplane is landing")
    def sleep(self):
        print("passengerplane is sleeping")

class cargoplane:
    def takeoff(self):
        print("cargoplane is taking off")
    def fly(self):
        print("cargoplane is flying")
    def land(self):
        print("cargoplane is landing")
    def sleep(self):
        print("cargoplane is sleeping")

class fighterplane:
    def takeoff(self):
        print("fighterplane is taking off")
    def fly(self):
        print("fighterplane is flying")
    def land(self):
        print("fighterplane is landing")
    def sleep(self):
        print("fighterplane is sleeping")

p=Passengerplane()
p.takeoff()
p.fly()
p.land()
p.sleep()
c=cargoplane()
c.takeoff()
c.fly()
c.land()
c.sleep()
f=fighterplane()
f.takeoff()
f.fly()
f.land()
f.sleep()

#Implementation of inheritance
class plane:
    def takeoff(self):
        print("plane is taking off")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class passengerplane:
    def carry_p(self):
        print("passengerplane is carrying p")

class cargoplane:
    def carry_c(self):
        print("cargoplane is carrying c")

class fighterplane:
    def carry_f(self):
        print("fighterplane is carrying f")
z=plane()
p=passengerplane()
c=cargoplane()
f=fighterplane()
z.takeoff()
z.fly()
z.land()
p.carry_p()
c.carry_c()
f.carry_f()

#access method from child class but in child class not include any methods
class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def hunt(self):
        print("animal is hunting")

class lion(animal):
    pass
class tiger(animal):
    pass
class fox(animal):
    pass
l=lion()
t=tiger()
f=fox()
l.eat()
l.sleep()
l.hunt()
t.eat()
t.sleep()
t.hunt()
f.eat()
f.sleep()
f.hunt()
f.eat()
f.sleep()
f.hunt()

