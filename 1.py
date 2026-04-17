#keywords in python(35 keywords iin python)
import keyword
print(keyword.kwlist)
print(f"Number of keywords: {len(keyword.kwlist)}")

#constructor : it is special type of function is automatically called when an object of a class is instantiated.
class Fan:   #class
    def __init__(self):     #constructor
        self.brand="usha"   #instance variable
        self.color="white"
        self.cost=3000
        self.wings=3
    def on(self):           #methods
        print("fan is on")
    def rotate(self):
        print("fan is rotating")
    def off(self):
        print("fan is off")
f1=Fan()        #printing the variable
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.wings)
f1.on()     #calling the method
f1.rotate()
f1.off()


#example 2
class student:
    def __init__(self):
        self.name="lokesh"
        self.age=21
        self.usn=420
    def study(self):
        print("lokesh is studying")
s=student()
print(s.name)
print(s.age)
print(s.usn)
s.study()

#Practice
class pg():
    def __init__(self):
        self.name ='RIO PG FOR GENTS'
        self.area="BTM LAYOUT"
        self.status='4 sharing'
        self.cost=5500
    def food(self):
        print(f"{self.name} in dosa is today's Tiffin")
        print(f"{self.area} is a location of this PG")
PG=pg()
print(PG.name)
print(PG.area)
print(PG.status)
print(PG.cost)
PG.food()
