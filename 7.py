#Instance variable and static variable

class TV:
    def __init__(self):
        self.brand = "SAMSUNG"  #instance variable
        self.cost = 25000       #instance variable

    def display(self):
        self.color = "black"
        print(self.color)

T1 = TV()
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