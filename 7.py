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
