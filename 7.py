#standard way to write a class
class student:
    def __init__(self,name,age):    #name and age is parameters
        self.name = name
        self.age = age
s1=student("Abhi",21)   # values accepted by parameters
print(s1.name)
print(s1.age)
s2=student("Ram",22)
print(s2.name)
print(s2.age)

class mobile:
    def __init__(self, name,price,color):
        self.name = name
        self.price = price
        self.color = color
m1=mobile("vivo",21000,"purple")
print(m1.name)
print(m1.price)
print(m1.color)
print(m1.name,m1.price,m1.color)

m2=mobile("oppo",26000,"white")
print(m2.name)
print(m2.price)
print(m2.color)
print(m2.name,m2.price,m2.color)

#varies way to declare the instance variable (inside the constructor, inside the methods, outside the class)
class clg:
    def __init__(self):
        self.clgname = "GEC Challakere" #inside the constructor
    def clsroom(self):
        self.rooms= 50  #inside the methods
        self.smrroom = 3    #inside the methods
    def door(self):
        self.maindoor = 1   #inside the methods
        self.doors="every rooms have a door"    #inside the methods
c1=clg()
print(c1.clgname)
c1.clsroom()
print(c1.rooms)
print(c1.smrroom)
c1.facultiesroom = "20+"    #outside the class(using reference object)
print(c1.facultiesroom)
c1.door()
print(c1.maindoor)
print(c1.doors)


#Instance variable and static variable
class TV:
    price= 21000    #static variable
    def __init__(self):
        self.brand = "SAMSUNG"  #instance variable
        self.cost = 25000       #instance variable

    def display(self):
        self.color = "black"
        print(self.color)

T1 = TV()
print(T1.price)
print(T1.brand)
print(T1.cost)
T1.display()  #method only run when method is call
print(T1.color)  #before calling method you print method its shows the error
T1.size = 36  #variable create outside the class
print(T1.size)


#loan program
class Farmer:
    r=2.5   #static variable
    def __init__(self,p,t):
        self.principle = p      #instance variable
        self.time = t           #instance variable
    def loan(self):
        si=(self.principle*self.time*Farmer.r)/100
        print(si)
f1=Farmer(200000,4)
f2=Farmer(500000,5)
f1.loan()
f2.loan()
print(Farmer.r)


class hero:
    wife = "Vijaya Lakshmi" #static variable

    def __init__(self, name, age, movie):
        self.name = name    #instance variable
        self.age = age      #instance variable
        self.movies = movie #instance variable

    def fimaly(self):
        print(f"Darshan wife is {hero.wife}")   #access the static variable in method using class name


h1 = hero("Darshan", 52, 54)
print(h1.name, h1.age, h1.movies)
h1.area = "RR nagara"
print(h1.area)

h1.fimaly() #calling method