#static method and class method

'''
In static and class methods we mention method name in decorator using @
'''

class Mobile:
    def __init__(self):
        self.name = "nokia"
    def call(self):
        print("mobile is ringing")

    @staticmethod
    def charge():
        print("mobile is charging")

    @classmethod
    def hang(cls):
        print("mobile is hanging")
m1=Mobile()
m1.call()
m1.charge()
m1.hang()
Mobile.charge()
Mobile.hang()

class Mobile:
    def battery(self):
        self.charge= "80%"

    @staticmethod
    def call():
        recharge="Recharge complete successfully"
        return recharge

    @classmethod
    def color(cls):
        cls.color1 = "purple"
        cls.color2 = "blue"
        cls.color3 = "green"
        return f"{cls.color1}, {cls.color2}, {cls.color3}"

m1=Mobile()
m1.battery()
print(m1.charge)
print(m1.call())
print(m1.color())
class Calci:
    def operation(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4
c=Calci()
r1=c.operation(1,2)
print(r1)   #In python default tuple will print
r1,r2,r3,r4=c.operation(5,2)    #it takes single value
print(r1)
print(r2)
print(r3)
print(r4)

class college:
    def clsroom(self):
        self.rooms = 15
        print("15+ classrooms in college")

    @classmethod
    def seminar(cls):
        cls.smrhall= 3
        print("Total seminar hall in college ")

    @staticmethod
    def faculty():
        print("30+ faculties")

c1=college()
c1.clsroom()
print(c1.rooms)
c1.seminar()
print(c1.smrhall)
c1.faculty()

#default argument and keyword argument
class demo:
    def disp(self,a=10,b=20,c=30):
        print(a,b,c)
d=demo()
x=11
y=22
z=33
d.disp() #10,20,30
d.disp(x,y,z)   #11,22,33
d.disp(z)   #33,20,30
d.disp(y,z) #22,33,30
d.disp(a=z,b=y,c=x) #33,22,11
d.disp(c=y) #10,20,22

#Method return multiple values
class calci:
    def operation(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4  #python automatically pack these into a tuple like (c1,c2,c3,c4)
c1=calci()
res=c1.operation(1,2)
print(res)  #(3,-1,2,0.5)
r1,r2,r3,r4 = c1.operation(3,4) #Now tuple automatically unpacks
print(r1,r2,r3,r4)  #7 -1 12 0.75
print(r1)   #7
print(r2)   #-1
print(r3)   #12
print(r4)   #0.75

