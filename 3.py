#adding , modifying, deleting the variable outside the class
class Heroine:
    def __init__(self):
        self.name= "Rukku"
        self.age=28
        self.numOfMovies=7
    def act(self):
        print("Rukku is good actress")
h=Heroine()
print(h.name,h.age,h.numOfMovies)
#crete a variable outside the class using reference variable
h.addr="Karnataka"  #adding
print(h.addr)
h.age=29 #modifing
print(h.age)
del h.numOfMovies   #deleting(after when delete a variable you print that variable PVM gives an error for this print

#consider car is one object and write the program which should min 3 variable and 2 method
class Car:
    def __init__(self):
        self.name="Rolls Royce"
        self.color="Black"
        self.cost= "5 cr"
    def speed(self):
        print("This car speed is 180km/h")
    def status(self):
        print("This car satus is 100km/h")
c=Car()
print(c.name)
print(c.color)
c.speed()
c.status()

class Bike:
    def __init__(self):    #apart from we use any keyword replace with "self",but using self is a standard way
        self.brand="Royal Enfield"
        self.model=1990
        self.color="Black"
    def start(self):
        print(self.brand)
        print(self)    #print the address of the self keyword
b=Bike()
print(b.brand)
print(b.model)
print(b.color)
b.start()
print(b)   #print the address of the reference variable


#pracrice
class abc:
    def __init__(what):    #we can use anything as a keyword self or other, but self is a standard way
        what.a="abhi"
        what.b="ravi"
    def study(what):
        print(f"{what.a} and {what.b} both are studying")
    def lazy(what):
        print(f"but, {what.a} is lazy")
        print(what.b)
        print(what.a)
        print(what)
z=abc()
print(z.a)
print(z.b)
z.study()
z.lazy()
print(id(z))
print(z)
